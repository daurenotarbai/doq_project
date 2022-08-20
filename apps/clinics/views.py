import datetime
from django.db.models import Avg, Count, Min, Q, IntegerField
from django.db.models.functions import Cast
from django.http import HttpResponse
from django.utils import timezone
from elasticsearch_dsl import Q as EQ
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from apps.clinics.elesticsearch import ClinicParametrsDocument, DoctorParametrsDocument, \
    ProcedureParametrsDocument, \
    SpecialityParametrsDocument
from apps.clinics.models import Speciality, Procedure, Clinic, Doctor, AppointmentDoctorTime, \
    WeekDaysNumber, ClinicApplication
from apps.clinics.serializers import SpecialitySerializer, ProcedureSerializer, ClinicSerializer, \
    ClinicDetailSerializer, ClinicSearchSerializer, DoctorSearchSerializer, \
    SpecialitySearchSerializer, \
    ProcedureSearchSerializer, DoctorSerializer, \
    AppointmentDoctorTimeSerializer, \
    DoctorDetailSerializer, DoctorCommentSerializer, \
    ClinicApplicationCreateSerializer
from apps.patients.models import Comment


class ClinicApplicationCreateView(CreateAPIView):
    queryset = ClinicApplication
    serializer_class = ClinicApplicationCreateSerializer


class SpecialitiesView(APIView):
    def get(self, obj):
        queryset = Speciality.objects.all()
        serializer = SpecialitySerializer(queryset, many=True)
        return Response(serializer.data)


class SpecialitiesDetailView(RetrieveAPIView):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer


class ProceduresView(APIView):
    permission_classes = [AllowAny]

    def get(self, obj):
        queryset = Procedure.objects.filter(parent=None)
        serializer = ProcedureSerializer(queryset, many=True)
        return Response(serializer.data)


class ProceduresDetailView(RetrieveAPIView):
    queryset = Procedure.objects.all()
    serializer_class = ProcedureSerializer


class ClinicDoctorsView(ListAPIView):
    model = Doctor
    serializer_class = DoctorSerializer

    def get_queryset(self):
        clinic_id = self.kwargs.get('clinic_id')
        queryset = self.model.objects.filter(clinic=clinic_id)
        return queryset


class ProcedureDoctorsView(ClinicDoctorsView):

    def get_queryset(self):
        req_get = self.request.GET
        procedure_id = self.kwargs.get('procedure_id')
        sort_by_rating = req_get.get('by_rating')
        sort_by_price = req_get.get('procedure_fee')
        sort_by_for_child = req_get.get('for_child')
        sort_by_experience_years = req_get.get('by_experience_years')
        date = req_get.get('date')
        procedure = Procedure.objects.get(id=procedure_id)
        queryset = self.model.objects.filter(procedures__exact=procedure)
        if sort_by_for_child:
            queryset = queryset.filter(for_child=True)
        if date:
            queryset = queryset.filter(appoint_times__date=date)
        if sort_by_rating:
            queryset = queryset.order_by('-score')
        elif sort_by_price:
            queryset = queryset.order_by('doctor_procedures__price')
        elif sort_by_experience_years:
            queryset = queryset.order_by('operates_from')

        return queryset.annotate(procedure_id=Cast(procedure_id, IntegerField()))


class SpecialityDoctorsView(ClinicDoctorsView):

    def get_queryset(self):
        req_get = self.request.GET
        sort_by_rating = req_get.get('by_rating')
        sort_by_price = req_get.get('consultation_fee')
        sort_by_experience_years = req_get.get('by_experience_years')
        speciality_id = self.kwargs.get('speciality_id')
        sort_by_for_child = req_get.get('for_child')
        date = req_get.get('date')
        speciality = Speciality.objects.get(id=speciality_id)
        queryset = self.model.objects.filter(specialities__exact=speciality)
        if sort_by_for_child:
            queryset = queryset.filter(for_child=True)
        if date:
            queryset = queryset.filter(appoint_times__date=date)
        if sort_by_rating:
            queryset = queryset.order_by('-score')
        elif sort_by_price:
            queryset = queryset.order_by('consultation_fee')
        elif sort_by_experience_years:
            queryset = queryset.order_by('operates_from')
        return queryset.annotate(speciality_id=Cast(speciality_id, IntegerField()))


class DoctorsDetailView(RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorDetailSerializer


class DoctorCommentsView(ListAPIView):
    model = Comment
    serializer_class = DoctorCommentSerializer

    def get_queryset(self):
        doctor_id = self.kwargs.get('doctor_id')
        queryset = self.model.objects.filter(doctor=doctor_id)
        return queryset


class ClinicCommentsView(ListAPIView):
    model = Comment
    serializer_class = DoctorCommentSerializer

    def get_queryset(self):
        clinic_id = self.kwargs.get('clinic_id')
        queryset = self.model.objects.filter(doctor__clinic__id=clinic_id)

        return queryset


class DoctorAppointmentTimesView(ListAPIView):
    queryset = AppointmentDoctorTime
    serializer_class = AppointmentDoctorTimeSerializer

    def get_queryset(self):
        doctor_id = self.kwargs.get('doctor_id')
        address_id = self.kwargs.get('address_id')
        queryset = self.queryset.objects.filter(
            doctor=doctor_id,
            clinic_address=address_id,
            date__gte=datetime.datetime.today()
        )
        return queryset


class ClinicsViewSet(viewsets.ModelViewSet):
    queryset = Clinic.objects.filter(is_active=True).prefetch_related('addresses').annotate(
        avr_doctors_score=Avg('doctors__score', distinct=True, default=0.0),
        comment_number=Count('doctors__comments', distinct=True)).order_by('avr_doctors_score')
    serializer_class = ClinicSerializer

    def get_queryset(self):
        sort_by_rating = self.request.GET.get('by_rating')
        filter_by_24_hours = self.request.GET.get('24_hours')
        filter_by_is_open = self.request.GET.get('is_open')
        if filter_by_is_open:
            ids = []
            for clinic in self.queryset:
                for address in clinic.addresses.all():
                    for schedule in address.schedules.all():
                        for key, value in WeekDaysNumber.items():
                            now = timezone.now()
                            if timezone.localtime(now).weekday() == value:
                                if key == schedule.day_in_week:
                                    time_now = timezone.localtime(now).time()
                                    if schedule.end_day > time_now:
                                        ids.append(clinic.id)
            self.queryset = self.queryset.filter(id__in=ids)
        if filter_by_24_hours:
            self.queryset = self.queryset.filter(addresses__is_24_hours=True)
        if sort_by_rating:
            queryset = self.queryset.order_by('-avr_doctors_score')
            return queryset
        return self.queryset

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
                EQ('query_string', query=query, fields=['name'])).execute()
            doctor = DoctorParametrsDocument.search().query(
                EQ('query_string', query=query, fields=['first_name', 'last_name', 'middle_name'])).execute()
            procedure = ProcedureParametrsDocument.search().query(
                EQ('query_string', query=query, fields=['name'])).execute()
            speciality = SpecialityParametrsDocument.search().query(
                EQ('query_string', query=query, fields=['name'])).execute()
            clinic_serializer = ClinicSearchSerializer(clinic, many=True)
            doctor_serializer = DoctorSearchSerializer(doctor, many=True)
            procedure_serializer = ProcedureSearchSerializer(procedure, many=True)
            speciality_serializer = SpecialitySearchSerializer(speciality, many=True)
            data = {'clinics': clinic_serializer.data,
                    'doctors': doctor_serializer.data,
                    'specialities': speciality_serializer.data,
                    'procedures': procedure_serializer.data,
                    }
            return Response(data)

        except Exception as e:
            return HttpResponse(e, status=500)
