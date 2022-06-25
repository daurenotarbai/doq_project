from rest_framework import serializers
from apps.clinics.models import Speciality, Procedure, Clinic, Address, Doctor, AppointmentDoctorTime, AppointmentTime


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
    description = serializers.SerializerMethodField()

    class Meta:
        model = Clinic
        fields = ['id','logo', 'name', 'addresses', 'description']

    def get_description(self, obj):
        return obj.description[:160] + "..."


class ClinicWithAppointmentsSerializer(serializers.ModelSerializer):
    addresses = AddressWithAppointmentTimesSerializer(many=True)
    description = serializers.SerializerMethodField()

    class Meta:
        model = Clinic
        fields = ['id', 'name', 'addresses', 'description']

    def get_description(self, obj):
        return obj.description[:160] + "..."


class DoctorSerializer(serializers.ModelSerializer):
    specialities = SpecialitySearchSerializer(many=True)
    clinic = serializers.CharField()

    class Meta:
        model = Doctor
        exclude = ['gender', 'procedures', 'created_at', 'changed_at']


class SpecialityDetailSerializer(serializers.HyperlinkedModelSerializer):
    doctors = DoctorSerializer(many=True)

    class Meta:
        model = Speciality
        fields = ['url', 'name', 'doctors']


class ClinicDetailSerializer(serializers.HyperlinkedModelSerializer):
    addresses = AddressSerializer(many=True)
    doctors = DoctorSerializer(many=True)

    class Meta:
        model = Clinic
        fields = ('url', 'id', 'name', 'logo', 'description', 'doctors', 'addresses')
