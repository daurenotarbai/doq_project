import datetime

from rest_framework import serializers

from apps.clinics.models import Doctor, AppointmentDoctorTime
from apps.clinics.serializers import SpecialitySearchSerializer
from apps.patients.models import Appointment, Comment, Patient


class DoctorBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'photo']


class DoctorBaseWithSpecialitySerializer(serializers.ModelSerializer):
    specialities = SpecialitySearchSerializer(many=True)

    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'photo', 'specialities']


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


class AppointmentDoctorTimeSerializer(serializers.ModelSerializer):
    doctor = DoctorBaseSerializer()

    class Meta:
        model = AppointmentDoctorTime
        fields = ('id', 'doctor', 'date')


class ClientClinicAppointmentSerializer(serializers.ModelSerializer):
    patient = PatientBaseSerializer()
    appointment_doctor_time = AppointmentDoctorTimeSerializer()
    appointment_time = serializers.CharField()

    class Meta:
        model = Appointment
        fields = ('id', 'patient', 'appointment_time', 'appointment_doctor_time')


class FilterAppointmentDoctorTimeListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.exclude(date__lt=datetime.datetime.now().date())
        return super(FilterAppointmentDoctorTimeListSerializer, self).to_representation(data)


class ClientClinicAppointmentDoctorTimeSerializer(serializers.ModelSerializer):
    times = serializers.SerializerMethodField()

    class Meta:
        model = AppointmentDoctorTime
        fields = ('id', 'date', 'times')
        list_serializer_class = FilterAppointmentDoctorTimeListSerializer

    def get_times(self, obj):
        count_busy_times = 0
        appointments = Appointment.objects.filter(
            appointment_doctor_time__doctor__id=obj.doctor.id,
            )
        appointment_times_list = [
            appointment.appointment_time.start_time for appointment in appointments if
            obj.date == appointment.appointment_doctor_time.date
        ]
        ttimes = obj.times.all()
        for item in ttimes:
            if item.start_time in appointment_times_list:
                count_busy_times += 1
        return {'all_times':obj.times.count(), 'busy_time':count_busy_times}


class ClientClinicDoctorAppointmentTimeSerializer(serializers.ModelSerializer):
    appoint_times = ClientClinicAppointmentDoctorTimeSerializer(many=True)

    class Meta:
        model = Doctor
        fields = ('id', 'first_name', 'last_name', 'middle_name', 'photo', 'appoint_times')
