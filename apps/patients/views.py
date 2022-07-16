# Create your views here.
from rest_framework.generics import CreateAPIView

from apps.patients.models import Appointment, Patient
from apps.patients.serializers import PatientAppointmentCreateSerializer


class CreatePatientAppointmentView(CreateAPIView):
    queryset = Appointment
    serializer_class = PatientAppointmentCreateSerializer

    def create(self, request, *args, **kwargs):
        first_name = request.data.pop('name')
        iin = request.data.pop('iin')
        phone = request.data.pop('phone')
        patient, _ = Patient.objects.get_or_create(phone=phone, first_name=first_name, iin=iin)
        request.data['patient'] = patient.id
        return super(CreatePatientAppointmentView, self).create(request, *args, **kwargs)
