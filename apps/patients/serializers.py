from rest_framework import serializers

from apps.patients.models import Appointment


class PatientAppointmentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ('id', 'patient', 'appointment_time', 'appointment_doctor_time')