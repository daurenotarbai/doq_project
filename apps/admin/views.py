from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView

from apps.clinics.models import Doctor
from apps.clinics.serializers import DoctorSerializer


class ClientClinicDoctorsView(ListAPIView):
    model = Doctor
    serializer_class = DoctorSerializer

    def get_queryset(self):
        clinic_id = self.kwargs.get('clinic_id')
        print("REQ_USER", self.request.user.clinic)

        queryset = self.model.objects.filter(clinic=clinic_id)
        return queryset