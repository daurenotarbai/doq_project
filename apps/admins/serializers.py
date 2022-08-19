import datetime

from rest_framework import serializers

from apps.admins.models import MonthReport
from apps.clinics.models import Doctor, AppointmentDoctorTime, AppointmentTime, DoctorProcedures, \
    Address, DoctorSpecialities
from apps.clinics.serializers import SpecialitySearchSerializer, DoctorSerializer, \
    ProcedureSearchSerializer
from apps.patients.models import Appointment, Comment, Patient


class ClientClinicAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'address')


class ClientClinicAppointmentTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentTime
        fields = ['id', 'start_time']


class DoctorBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'photo', 'experience_years']


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
        fields = ('id', 'patient', 'appointment_time', 'appointment_doctor_time', 'is_visited')


class FilterAppointmentDoctorTimeListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.exclude(date__lt=datetime.datetime.now().date())
        return super(FilterAppointmentDoctorTimeListSerializer, self).to_representation(data)


class ClientClinicAppointmentDoctorTimeSerializer(serializers.ModelSerializer):
    times = serializers.SerializerMethodField()
    info = serializers.SerializerMethodField()

    class Meta:
        model = AppointmentDoctorTime
        fields = ('id', 'date', 'times', 'info')
        list_serializer_class = FilterAppointmentDoctorTimeListSerializer

    all_times = None
    busy_times = None

    def get_info(self, obj):

        return {
            'all_times': self.all_times,
            'busy_times': self.busy_times
        }

    def get_times(self, obj):
        appointments = Appointment.objects.filter(appointment_doctor_time__doctor__id=obj.doctor.id)

        appointment_times_list = [
            appointment.appointment_time.start_time for appointment in appointments if
            obj.date == appointment.appointment_doctor_time.date
        ]
        self.all_times = obj.times.all().count()
        ttimes = obj.times.all()
        times_list = []
        count = 0
        for item in ttimes:
            test_dict = {
                'id': item.id,
                'start_time': item.start_time,
                'is_free': True
            }
            if item.start_time in appointment_times_list:
                test_dict['is_free'] = False
                count += 1

            times_list.append(test_dict)
        self.busy_times = count
        return times_list


class ClientClinicDoctorAppointmentTimeSerializer(serializers.ModelSerializer):
    appoint_times = serializers.SerializerMethodField()
    address_id = serializers.IntegerField()

    class Meta:
        model = Doctor
        fields = (
            'id', 'first_name',
            'last_name', 'middle_name',
            'photo', 'appoint_times',
            'address_id',
        )

    def get_appoint_times(self, obj):
        serializer = ClientClinicAppointmentDoctorTimeSerializer(
            data=obj.appoint_times.filter(clinic_address=obj.address_id),
            many=True, )
        serializer.is_valid()
        return serializer.data


class AppointmentDoctorTimeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentDoctorTime
        fields = ('id', 'date', 'doctor', 'clinic_address', 'times')


class ClientClinicTotalReconciliationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthReport
        fields = ('id', 'month', 'verified', 'total_appointments', 'status')


class ClientClinicDoctorProceduresSerializer(serializers.ModelSerializer):
    procedure = ProcedureSearchSerializer(read_only=True)
    procedure_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = DoctorProcedures
        fields = '__all__'


class ClientClinicDoctorProceduresUpdateSerializer(ClientClinicDoctorProceduresSerializer):
    class Meta:
        model = DoctorProcedures
        exclude = ['doctor']


class ClientClinicDoctorSpecialitiesSerializer(serializers.ModelSerializer):
    speciality = SpecialitySearchSerializer(read_only=True)
    speciality_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = DoctorSpecialities
        fields = '__all__'


class ClientClinicDoctorSpecialitiesUpdateSerializer(ClientClinicDoctorSpecialitiesSerializer):
    class Meta:
        model = DoctorSpecialities
        exclude = ['doctor']


class ClientClinicDoctorDetailSerializer(DoctorSerializer):
    doctor_procedures = ClientClinicDoctorProceduresSerializer(many=True)
    doctor_specialities = ClientClinicDoctorSpecialitiesSerializer(many=True)

    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'photo', 'experience_years',
                  'consultation_fee', 'clinic', 'doctor_specialities', 'doctor_procedures']
