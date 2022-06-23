from rest_framework import serializers
from apps.clinics.models import Speciality, Procedure, Clinic, Address, Doctor


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
        fields = ('address', 'clinic')


class ClinicSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True)
    description = serializers.SerializerMethodField()

    class Meta:
        model = Clinic
        fields = ['id', 'name', 'addresses', 'description']

    def get_description(self, obj):
        return obj.description[:160] + "..."


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


class DoctorSerializer(serializers.ModelSerializer):
    specialities = SpecialitySearchSerializer(many=True)

    class Meta:
        model = Doctor
        exclude = ['gender', 'procedures']


class ClinicDetailSerializer(serializers.HyperlinkedModelSerializer):
    addresses = AddressSerializer(many=True)
    doctors = DoctorSerializer(many=True)

    class Meta:
        model = Clinic
        fields = ('url', 'id', 'name', 'logo', 'description', 'doctors', 'addresses')
