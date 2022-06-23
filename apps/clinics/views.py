from django.http import HttpResponse
from elasticsearch_dsl import Q
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.clinics.elesticsearch import ClinicParametrsDocument, DoctorParametrsDocument, ProcedureParametrsDocument, \
    SpecialityParametrsDocument
from apps.clinics.models import Speciality, Procedure, Clinic, Doctor
from apps.clinics.serializers import SpecialitySerializer, ProcedureSerializer, ClinicSerializer, \
    ClinicDetailSerializer, ClinicSearchSerializer, DoctorSearchSerializer, SpecialitySearchSerializer, \
    ProcedureSearchSerializer


class SpecialitiesViewSet(viewsets.ModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer


class ProceduresViewSet(viewsets.ModelViewSet):
    queryset = Procedure.objects.filter(parent=None)
    serializer_class = ProcedureSerializer


class ClinicsViewSet(viewsets.ModelViewSet):
    queryset = Clinic.objects.filter(is_active=True).prefetch_related('addresses')
    serializer_class = ClinicSerializer

    def retrieve(self, request, *args, **kwargs):
        context = {
            'request': request
        }
        instance = self.get_object()
        serializer = ClinicDetailSerializer(instance, context=context)
        return Response(serializer.data)


class MainSearchClinicView(APIView, LimitOffsetPagination):
    search_document = ClinicParametrsDocument

    def get(self, request, query):
        try:
            clinic = ClinicParametrsDocument.search().query(
                Q('query_string', query=query, fields=['name'])).execute()
            doctor = DoctorParametrsDocument.search().query(
                Q('query_string', query=query, fields=['first_name', 'last_name'])).execute()
            procedure = ProcedureParametrsDocument.search().query(
                Q('query_string', query=query, fields=['name'])).execute()
            speciality = SpecialityParametrsDocument.search().query(
                Q('query_string', query=query, fields=['name'])).execute()
            clinic_serializer = ClinicSearchSerializer(clinic, many=True)
            doctor_serializer = DoctorSearchSerializer(doctor, many=True)
            procedure_serializer = ProcedureSearchSerializer(procedure, many=True)
            speciality_serializer = SpecialitySearchSerializer(speciality, many=True)
            data = {'clinics': clinic_serializer.data, 'doctors': doctor_serializer.data,
                    'specialities': speciality_serializer.data, 'procedures': procedure_serializer.data}
            return Response(data)

        except Exception as e:
            return HttpResponse(e, status=500)


@api_view(('GET',))
def main_for_test(request):
    doctors = Doctor.objects.all().prefetch_related('procedures').select_related('clinic')
    clinics = Clinic.objects.all().prefetch_related('doctors')
    for i in doctors:
        print(i.first_name, i.clinic.name)
    for j in clinics:
        print(j.name, [d for d in j.doctors.all()])
    return Response({"data": 1})
