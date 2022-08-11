from rest_framework import serializers

from apps.patients.models import Appointment, Comment


class PatientAppointmentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ('id', 'patient', 'appointment_time', 'appointment_doctor_time')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'text', 'star', 'parent', 'doctor', 'patient')