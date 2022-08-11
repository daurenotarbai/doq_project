from rest_framework import serializers

from apps.clinics.models import Doctor
from apps.patients.models import Appointment, Comment, Patient


class DoctorBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'photo']


class PatientBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'first_name', 'phone']


class ClientClinicDoctorsSerializer(serializers.ModelSerializer):
    specialities = serializers.SerializerMethodField()
    procedures = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = ('id', 'first_name', 'last_name', 'middle_name', 'photo',
                  'specialities', 'procedures', 'is_active')

    def get_specialities(self, obj) -> str:
        specialities = ', '.join([speciality.name for speciality in obj.specialities.all()])
        return specialities

    def get_procedures(self, obj) -> str:
        procedures = ', '.join([procedures.name for procedures in obj.procedures.all()])
        return procedures


class ClientClinicFeedbacksSerializer(serializers.ModelSerializer):
    doctor = DoctorBaseSerializer()
    patient = PatientBaseSerializer()
    visit_date = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'text', 'star', 'parent', 'doctor', 'patient', 'visit_date')

    def get_visit_date(self, obj):
        time = obj.patient.appointments.filter(
            appointment_doctor_time__doctor=obj.doctor,
        ).first()
        time = f'{time.appointment_doctor_time.date}, {time.appointment_time.start_time}'[:17]
        return time
