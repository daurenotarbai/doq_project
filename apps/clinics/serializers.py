import datetime

from django.db.models import Min
from rest_framework import serializers

from apps.admins.models import TermsOfUse
from apps.clinics.models import Speciality, Procedure, Clinic, Address, Doctor, \
    AppointmentDoctorTime, AppointmentTime, DoctorProcedures, WeekDaysNumber, \
    ClinicApplication, ClinicImage, DoctorCategory, DoctorSpecialities
from apps.core.models import City
from apps.patients.models import Comment, Patient, Appointment


class ProcedureSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields = ['id', 'name']


class ClinicSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ['id', 'name']


class SpecialitySearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ['id', 'name']


class DoctorSearchSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = ['id', 'name']

    def get_name(self, obj):
        return ("%s %s %s" % (obj.first_name, obj.last_name, obj.middle_name)).strip()


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'slug']


class SpecialitySerializer(serializers.ModelSerializer):
    doctor_number = serializers.SerializerMethodField()

    class Meta:
        model = Speciality
        fields = ['id', 'name', 'doctor_number']

    def get_doctor_number(self, obj):
        return obj.doctors.all().count()


class FilterHasDoctorListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.exclude(doctor_procedures=None)
        return super(FilterHasDoctorListSerializer, self).to_representation(data)


class SubProcedureSerializer(serializers.ModelSerializer):
    min_price = serializers.SerializerMethodField()

    class Meta:
        model = Procedure
        fields = ('id', 'name', 'min_price')
        list_serializer_class = FilterHasDoctorListSerializer

    def get_min_price(self, obj):
        min_price = obj.doctor_procedures.all().aggregate(min_price=Min('price'))
        return min_price.get('min_price')


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
        if obj.start_day or obj.end_day:
            return f'{obj.start_day} - {obj.end_day}'
        return '-'


class AddressSerializer(serializers.ModelSerializer):
    schedules = ScheduleSerializer(many=True)
    title = serializers.SerializerMethodField()

    class Meta:
        model = Address
        fields = ('id', 'address', 'title', 'schedules', 'latitude', 'longitude')

    def get_title(self, obj):
        if obj.is_24_hours:
            return "Круглосуточно"
        for key, value in WeekDaysNumber.items():
            if datetime.datetime.today().weekday() == value:
                for day in obj.schedules.all():
                    if key == day.day_in_week:
                        title = f'Открыто до {day.end_day}'
                        return title


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
        ttimes = obj.times.all().order_by('start_time')
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
    avr_doctors_score = serializers.FloatField()
    comment_number = serializers.IntegerField()

    class Meta:
        model = Clinic
        fields = ['id', 'logo', 'name', 'addresses', 'short_description', 'avr_doctors_score',
                  'comment_number']


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'first_name']


class DoctorCommentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'text', 'parent', 'patient', 'star']


class DoctorCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorCategory
        fields = ['name']


class DoctorSerializer(serializers.ModelSerializer):
    specialities = serializers.SerializerMethodField()
    procedures = serializers.SerializerMethodField()
    categories = DoctorCategorySerializer(many=True)
    clinic = serializers.CharField()
    comments_number = serializers.SerializerMethodField()
    addresses = serializers.SerializerMethodField()
    consultation_fee = serializers.SerializerMethodField()
    new_price = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = ['id', 'first_name',
                  'last_name',
                  'middle_name',
                  'photo',
                  'experience_years',
                  'consultation_fee',
                  'new_price',
                  'clinic',
                  'specialities',
                  'procedures',
                  'score',
                  'comments_number',
                  'addresses',
                  'categories',
                  'is_top',
                  ]

    def get_comments_number(self, obj):
        return obj.comments.all().count()

    def get_consultation_fee(self, obj, price=True):
        try:
            specialty_price = obj.doctor_specialities.filter(
                speciality_id=obj.speciality_id).first()
            if price:
                return specialty_price.price
            else:
                return specialty_price.new_price
        except AttributeError:
            pass
        try:
            procedure_price = obj.doctor_procedures.filter(
                procedure_id=obj.procedure_id).first()
            if price:
                return procedure_price.price
            else:
                return procedure_price.new_price
        except AttributeError:
            pass
        if price:
            return obj.consultation_fee
        else:
            return obj.new_price

    def get_new_price(self, obj):
        return self.get_consultation_fee(obj, price=False)

    def get_specialities(self, obj):
        from apps.admins.serializers import ClientClinicDoctorSpecialitiesSerializer
        try:
            speciality = DoctorSpecialities.objects.filter(speciality_id=obj.speciality_id,
                                                           doctor_id=obj.id)
            return ClientClinicDoctorSpecialitiesSerializer(speciality, many=True).data

        except AttributeError:
            speciality_ids = obj.specialities.all().values_list('id', flat=True)
            speciality = DoctorSpecialities.objects.filter(speciality_id__in=speciality_ids,
                                                           doctor_id=obj.id)
            return ClientClinicDoctorSpecialitiesSerializer(speciality, many=True).data

    def get_procedures(self, obj):
        from apps.admins.serializers import ClientClinicDoctorProceduresSerializer
        try:
            procedure = DoctorProcedures.objects.filter(procedure_id=obj.speciality_id,
                                                        doctor_id=obj.id)
            return ClientClinicDoctorProceduresSerializer(procedure, many=True).data

        except AttributeError:
            procedure_ids = obj.procedures.all().values_list('id', flat=True)
            procedure = DoctorProcedures.objects.filter(procedure_id__in=procedure_ids,
                                                        doctor_id=obj.id)
            return ClientClinicDoctorProceduresSerializer(procedure, many=True).data

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
        fields = ['id', 'procedure_id', 'price', 'new_price']


class DoctorWithProceduresSerializer(DoctorSerializer):
    doctor_procedures = DoctorProceduresSerializer(many=True)

    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'photo', 'experience_years',
                  'consultation_fee', 'clinic', 'specialities', 'score', 'comments_number',
                  'addresses', 'doctor_procedures', 'is_top']


class DoctorDetailSerializer(DoctorSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'photo', 'experience_years',
                  'consultation_fee', 'new_price',
                  'clinic', 'specialities', 'procedures', 'score', 'comments_number', 'addresses', 'description',
                  'categories', 'is_top'
                  ]


class SpecialityDetailSerializer(serializers.HyperlinkedModelSerializer):
    doctors = DoctorSerializer(many=True)

    class Meta:
        model = Speciality
        fields = ['id', 'name', 'doctors']


class ClinicImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicImage
        fields = ['id', 'image', 'is_main']


class ClinicDetailSerializer(ClinicSerializer):
    images = ClinicImageSerializer(many=True)

    class Meta:
        model = Clinic
        fields = ['id', 'logo', 'name', 'addresses', 'phone', 'description',
                  'avr_doctors_score', 'comment_number', 'images']


class ClinicApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicApplication
        fields = '__all__'


class TermsOfUseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermsOfUse
        fields = '__all__'


class PrivacyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = TermsOfUse
        fields = '__all__'
