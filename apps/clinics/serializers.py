from rest_framework import serializers

from apps.clinics.models import Speciality, Procedure, Clinic, Address, Doctor, \
    AppointmentDoctorTime, AppointmentTime
from apps.patients.models import Comment, Patient


class ProcedureSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields = ['name']


class ClinicSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ['name']


class SpecialitySearchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Speciality
        fields = ['name']


class DoctorSearchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name']


class SpecialitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Speciality
        fields = ['url', 'name']


class SubProcedureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Procedure
        fields = ('url', 'id', 'name')


class ProcedureSerializer(serializers.HyperlinkedModelSerializer):
    subprocedures = SubProcedureSerializer(many=True)

    class Meta:
        model = Procedure
        fields = ('url', 'id', 'name', 'parent', 'is_specialty', 'subprocedures')


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('address',)


class AppointmentTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentTime
        fields = ('start_time',)


class AppointmentDoctorTimeSerializer(serializers.ModelSerializer):
    times = AppointmentTimeSerializer(many=True)

    class Meta:
        model = AppointmentDoctorTime
        fields = ('date', 'times')


class AddressWithAppointmentTimesSerializer(serializers.ModelSerializer):
    appoint_times = AppointmentDoctorTimeSerializer(many=True)

    class Meta:
        model = Address
        fields = ('address', 'appoint_times')


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
        fields = ['first_name']


class DoctorCommentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = Comment
        fields = ['text', 'parent', 'patient', 'star']


class DoctorSerializer(serializers.ModelSerializer):
    specialities = SpecialitySearchSerializer(many=True)
    clinic = serializers.CharField()
    comments_number = serializers.SerializerMethodField()
    addresses = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'photo', 'experience_years',
                  'consultation_fee',
                  'clinic',
                  'specialities', 'score', 'comments_number', 'addresses']

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
        fields = ['url', 'name', 'doctors']


class ClinicDetailSerializer(ClinicSerializer):
    class Meta:
        model = Clinic
        fields = ['id', 'logo', 'image', 'name', 'addresses', 'phone', 'description',
                  'avr_doctors_score', 'comment_number']
