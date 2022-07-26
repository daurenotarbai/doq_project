from abc import ABC

from rest_framework import serializers

from apps.clinics.models import Speciality, Procedure, Clinic, Address, Doctor, \
    AppointmentDoctorTime, AppointmentTime, DoctorProcedures, Schedules
from apps.patients.models import Comment, Patient, Appointment


class ProcedureSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields = ['name']


class ClinicSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ['name']


class SpecialitySearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ['name']


class DoctorSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name']


class SpecialitySerializer(serializers.ModelSerializer):
    doctor_number = serializers.SerializerMethodField()

    class Meta:
        model = Speciality
        fields = ['id', 'name', 'doctor_number']

    def get_doctor_number(self, obj):
        return obj.doctors.all().count()


class SubProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields = ('id', 'name')


class ProcedureSerializer(serializers.ModelSerializer):
    subprocedures = SubProcedureSerializer(many=True)
    doctor_number = serializers.SerializerMethodField()

    class Meta:
        model = Procedure
        fields = ('id', 'name', 'parent', 'is_specialty', 'subprocedures', 'doctor_number')

    def get_doctor_number(self, obj):
        return obj.doctors.all().count()


class ScheduleSerializer(serializers.Serializer):
    day = serializers.SerializerMethodField()
    times = serializers.SerializerMethodField()

    def get_day(self, obj):
        return f'{obj.day_in_week}'

    def get_times(self, obj):
        return f'{obj.start_day} - {obj.end_day}'


class AddressSerializer(serializers.ModelSerializer):
    schedules = ScheduleSerializer(many=True)

    class Meta:
        model = Address
        fields = ('id', 'address', 'schedules')


class AppointmentTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentTime
        fields = ('id', 'start_time',)


class AppointmentDoctorTimeSerializer(serializers.ModelSerializer):
    times = serializers.SerializerMethodField()

    class Meta:
        model = AppointmentDoctorTime
        fields = ('id', 'date', 'doctor', 'times')

    def get_times(self, obj):
        appointments = Appointment.objects.filter(appointment_doctor_time__doctor__id=obj.doctor.id)

        appointment_times_list = [
            appointment.appointment_time.start_time for appointment in appointments if
            obj.date == appointment.appointment_doctor_time.date
        ]
        ttimes = obj.times.all()
        times_list = []
        for item in ttimes:
            test_dict = {
                'id': item.id,
                'start_time': item.start_time,
                'is_free': True
            }
            if item.start_time in appointment_times_list:
                test_dict['is_free'] = False
            times_list.append(test_dict)
        return times_list


class AddressWithAppointmentTimesSerializer(serializers.ModelSerializer):
    appoint_times = AppointmentDoctorTimeSerializer(many=True)

    class Meta:
        model = Address
        fields = ('id', 'address', 'appoint_times')


class ClinicSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True)
    short_description = serializers.SerializerMethodField()
    avr_doctors_score = serializers.FloatField()
    comment_number = serializers.IntegerField()

    class Meta:
        model = Clinic
        fields = ['id', 'logo', 'name', 'addresses', 'short_description', 'avr_doctors_score',
                  'comment_number']

    def get_short_description(self, obj):
        return obj.description[:160] + "..."


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'first_name']


class DoctorCommentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'text', 'parent', 'patient', 'star']


class DoctorSerializer(serializers.ModelSerializer):
    specialities = SpecialitySearchSerializer(many=True)
    clinic = serializers.CharField()
    comments_number = serializers.SerializerMethodField()
    addresses = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'photo', 'experience_years',
                  'consultation_fee', 'clinic', 'specialities', 'score', 'comments_number',
                  'addresses']

    def get_comments_number(self, obj):
        return obj.comments.all().count()

    def get_addresses(self, obj):
        data = []
        for address in obj.clinic.addresses.all():
            address = {
                "id": address.id,
                "address": address.address,
            }
            data.append(address)
        return data


class DoctorProceduresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DoctorProcedures
        fields = ['id', 'procedure_id', 'price']


class DoctorWithProceduresSerializer(DoctorSerializer):
    doctor_procedures = DoctorProceduresSerializer(many=True)

    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'photo', 'experience_years',
                  'consultation_fee', 'clinic', 'specialities', 'score', 'comments_number',
                  'addresses', 'doctor_procedures']


class DoctorDetailSerializer(DoctorSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'photo', 'experience_years',
                  'consultation_fee',
                  'clinic', 'specialities', 'score', 'comments_number', 'addresses', 'description']


class SpecialityDetailSerializer(serializers.HyperlinkedModelSerializer):
    doctors = DoctorSerializer(many=True)

    class Meta:
        model = Speciality
        fields = ['id', 'name', 'doctors']


class ProcedureDetailSerializer(serializers.HyperlinkedModelSerializer):
    doctors = DoctorWithProceduresSerializer(many=True)

    class Meta:
        model = Procedure
        fields = ['id', 'url', 'name', 'doctors']


class ClinicDetailSerializer(ClinicSerializer):
    class Meta:
        model = Clinic
        fields = ['id', 'logo', 'image', 'name', 'addresses', 'phone', 'description',
                  'avr_doctors_score', 'comment_number']
