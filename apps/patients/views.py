# Create your views here.
from rest_framework import exceptions
from rest_framework.generics import CreateAPIView

from apps.clinics.models import AppointmentDoctorTime
from apps.patients.models import Appointment, Patient, Comment
from apps.patients.serializers import PatientAppointmentCreateSerializer, CommentCreateSerializer


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
        patient, _ = Patient.objects.update_or_create(iin=iin, defaults={
            'phone': phone,
            'first_name': first_name,
        })
        request.data['patient'] = patient.id
        return super(CreatePatientAppointmentView, self).create(request, *args, **kwargs)


class CreateCommentView(CreateAPIView):
    queryset = Comment
    serializer_class = CommentCreateSerializer

    def create(self, request, *args, **kwargs):
        phone = request.data.pop('patient_phone')
        doctor_id = request.data.get('doctor')
        appointment = Appointment.objects.filter(
            patient__phone=phone,
            appointment_doctor_time__doctor__id=doctor_id,
        ).exists()

        if not appointment:
            raise exceptions.NotAcceptable(
                f'There is no appointment with this phone number {phone}')
        patient = Patient.objects.get(phone=phone)
        request.data['patient'] = patient.id
        return super(CreateCommentView, self).create(request, *args, **kwargs)
