# Create your views here.
from rest_framework import exceptions
from rest_framework.generics import CreateAPIView

from apps.clinics.models import AppointmentDoctorTime
from apps.patients.models import Appointment, Patient
from apps.patients.serializers import PatientAppointmentCreateSerializer


class CreatePatientAppointmentView(CreateAPIView):
    queryset = Appointment
    serializer_class = PatientAppointmentCreateSerializer

    def create(self, request, *args, **kwargs):
        first_name = request.data.pop('name')
        iin = request.data.pop('iin')
        phone = request.data.pop('phone')
        appointment_time = request.data.get('appointment_time')
        appointment_doctor_times = AppointmentDoctorTime.objects.get(
            id=request.data.get('appointment_doctor_time'))
        time_ids = [time.id for time in appointment_doctor_times.times.all()]
        if appointment_time not in time_ids:
            raise exceptions.NotAcceptable(
                "doctor has no 'appointment_time' with id {}".format(appointment_time))
        patient, _ = Patient.objects.get_or_create(phone=phone, first_name=first_name, iin=iin)
        request.data['patient'] = patient.id
        return super(CreatePatientAppointmentView, self).create(request, *args, **kwargs)
