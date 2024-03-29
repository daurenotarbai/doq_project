import datetime

import xlwt
from django.db.utils import IntegrityError
from django.db.models import Q, IntegerField, TimeField
from django.db.models.functions import Cast
from django.http import HttpResponse
from rest_framework import permissions, status
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.admins.models import MonthReport
from apps.admins.serializers import ClientClinicDoctorsSerializer, ClientClinicFeedbacksSerializer, \
    ClientClinicAppointmentSerializer, \
    ClientClinicDoctorAppointmentTimeSerializer, AppointmentDoctorTimeCreateSerializer, \
    ClientClinicAppointmentTimeSerializer, ClientClinicTotalReconciliationsSerializer, \
    ClientClinicDoctorDetailSerializer, ClientClinicAddressSerializer, \
    ClientClinicDoctorSpecialitiesSerializer, ClientClinicDoctorProceduresSerializer, \
    ClientClinicDoctorSpecialitiesUpdateSerializer, ClientClinicDoctorProceduresUpdateSerializer, \
    DoctorAddressSerializer
from apps.clinics.models import Doctor, Clinic, AppointmentDoctorTime, AppointmentTime, Address, \
    DoctorSpecialities, DoctorProcedures, DoctorClinicAddress, DurationChoices, Procedure
from apps.clinics.serializers import ProcedureSerializer
from apps.core.paginations import ClientAdminPagination, HundredPagination
from apps.patients.models import Comment, Appointment


class ClientClinicAppointmentTimesView(ListAPIView):
    model = AppointmentTime
    serializer_class = ClientClinicAppointmentTimeSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = HundredPagination

    def get_queryset(self):
        address_id = self.kwargs.get('address_id')
        doctor_id = self.kwargs.get('doctor_id')
        doctor_address = DoctorClinicAddress.objects.get(address_id=address_id, doctor_id=doctor_id)
        queryset = self.model.objects.filter(
            code=doctor_address.duration)
        return queryset


class ClientClinicAddressView(ListAPIView):
    model = Address
    serializer_class = ClientClinicAddressSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = HundredPagination

    def get_queryset(self):
        queryset = self.model.objects.filter(
            clinic__user=self.request.user)
        return queryset


class ClientClinicDoctorsView(ListAPIView):
    model = Doctor
    serializer_class = ClientClinicDoctorsSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = ClientAdminPagination

    def get_queryset(self):
        address_id = self.kwargs.get('address_id')
        clinic_id = Clinic.objects.filter(user=self.request.user).first()
        queryset = self.model.objects.filter(clinic=clinic_id)
        query = self.request.GET.get('query')
        filter_by_is_active = self.request.GET.get('is_active')
        if query:
            queryset = queryset.filter(
                Q(first_name__icontains=query) | Q(
                    last_name__icontains=query) | Q(
                    last_name__icontains=query) | Q(
                    middle_name__icontains=query) | Q(
                    specialities__name__icontains=query) | Q(
                    procedures__name__icontains=query)).distinct()
        if filter_by_is_active == 'true':
            queryset = queryset.filter(doctor_address__is_active=True).distinct()
        elif filter_by_is_active == 'false':
            queryset = queryset.filter(doctor_address__is_active=False).distinct()
        return queryset.annotate(address=Cast(address_id, IntegerField()))


class ClientClinicDoctorsDetailView(APIView):

    def get(self, request, doctor_id, address_id):
        queryset = Doctor.objects.get(id=doctor_id)
        queryset.address = address_id
        serializer = ClientClinicDoctorDetailSerializer(queryset)
        return Response(serializer.data)

    def patch(self, request, doctor_id, address_id, format=None):
        doctor_address = DoctorClinicAddress.objects.get(doctor_id=doctor_id, address_id=address_id)
        serializer = DoctorAddressSerializer(doctor_address, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientClinicDoctorsSpecialityCreateView(CreateAPIView):
    model = DoctorSpecialities
    serializer_class = ClientClinicDoctorSpecialitiesSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class ClientClinicDoctorsSpecialitiesUpdateView(UpdateAPIView):
    queryset = DoctorSpecialities.objects.all()
    serializer_class = ClientClinicDoctorSpecialitiesUpdateSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=201)


class ClientClinicDoctorsProceduresUpdateView(UpdateAPIView):
    queryset = DoctorProcedures.objects.all()
    serializer_class = ClientClinicDoctorProceduresUpdateSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=201)


class ClientClinicDoctorsProcedureCreateView(CreateAPIView):
    model = DoctorProcedures
    serializer_class = ClientClinicDoctorProceduresSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=201)


class ClientClinicFeedbacksView(ListAPIView):
    model = Comment
    serializer_class = ClientClinicFeedbacksSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = ClientAdminPagination
    lookup_field = 'id'

    def get_queryset(self):
        queryset = Comment.objects.filter(doctor__clinic__user=self.request.user, parent=None)
        query = self.request.GET.get('query')
        filter_by_is_responded = self.request.GET.get('is_responded')
        star = self.request.GET.get('star')
        created_date = self.request.GET.get('created_date')
        if query:
            queryset = queryset.filter(
                Q(doctor__first_name__icontains=query) | Q(
                    doctor__last_name__icontains=query) | Q(
                    doctor__last_name__icontains=query) | Q(
                    doctor__middle_name__icontains=query) | Q(
                    doctor__specialities__name__icontains=query) | Q(
                    doctor__procedures__name__icontains=query)).distinct()
        if created_date:
            queryset = queryset.filter(created_at__year=created_date[:4],
                                       created_at__month=created_date[5:7],
                                       created_at__day=created_date[8:10],
                                       )
        if star:
            queryset = queryset.filter(star=star)
        if filter_by_is_responded == 'true':
            queryset = queryset.filter(is_responded=True)
        elif filter_by_is_responded == 'false':
            queryset = queryset.filter(is_responded=False)
        return queryset


class ClientClinicFeedbacksDetailView(RetrieveAPIView, CreateAPIView):
    model = Comment
    serializer_class = ClientClinicFeedbacksSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        comment_id = kwargs['id']
        text = request.data.get('text')
        self.model.objects.create(parent_id=comment_id, text=text)
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid()
        return Response(serializer.data, status=201)

    def get_queryset(self):
        queryset = self.model.objects.filter(doctor__clinic__user=self.request.user, parent=None)
        return queryset


class ClientClinicAppointmentsView(ListAPIView):
    model = Appointment
    serializer_class = ClientClinicAppointmentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = ClientAdminPagination

    def get_queryset(self):
        queryset = Appointment.objects.filter(
            appointment_doctor_time__doctor__clinic__user=self.request.user).order_by('-created_at')
        query = self.request.GET.get('query')
        visit_date = self.request.GET.get('visit_date')
        if query:
            queryset = queryset.filter(
                Q(appointment_doctor_time__doctor__first_name__icontains=query) | Q(
                    appointment_doctor_time__doctor__last_name__icontains=query) | Q(
                    appointment_doctor_time__doctor__last_name__icontains=query) | Q(
                    appointment_doctor_time__doctor__middle_name__icontains=query) | Q(
                    appointment_doctor_time__doctor__specialities__name__icontains=query) | Q(
                    appointment_doctor_time__doctor__procedures__name__icontains=query)).distinct()
        if visit_date:
            queryset = queryset.filter(appointment_doctor_time__date=visit_date)
        return queryset


class ClientClinicDoctorsAppointmentTimesView(ListAPIView):
    model = Doctor
    serializer_class = ClientClinicDoctorAppointmentTimeSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = ClientAdminPagination

    def get_queryset(self):
        address_id = self.kwargs.get('address_id')
        queryset = self.model.objects.filter(clinic__user=self.request.user,
                                             doctor_address__address=address_id,
                                             doctor_address__is_active=True).annotate(
            address_id=Cast(address_id, IntegerField()))
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(
                Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(
                    middle_name__icontains=query) | Q(specialities__name__icontains=query) | Q(
                    procedures__name__icontains=query)).distinct()
        return queryset


class ClientClinicDoctorsAppointmentTimesCreateView(CreateAPIView):
    model = AppointmentDoctorTime
    serializer_class = AppointmentDoctorTimeCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        doctor_id = kwargs['doctor_id']
        date = request.data.get('date')
        clinic_address = request.data.get('clinic_address')
        objects = self.model.objects.filter(doctor=doctor_id, date=date,
                                            clinic_address=clinic_address)
        objects.delete()
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(status=201)


class ClientClinicReconciliationsView(ListAPIView):
    model = Appointment
    serializer_class = ClientClinicAppointmentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = ClientAdminPagination

    def get_queryset(self):
        queryset = Appointment.objects.filter(
            appointment_doctor_time__doctor__clinic__user=self.request.user)
        query = self.request.GET.get('query')
        visit_date = self.request.GET.get('visit_date')
        if query:
            queryset = queryset.filter(
                Q(appointment_doctor_time__doctor__first_name__icontains=query) | Q(
                    appointment_doctor_time__doctor__last_name__icontains=query) | Q(
                    appointment_doctor_time__doctor__last_name__icontains=query) | Q(
                    appointment_doctor_time__doctor__middle_name__icontains=query) | Q(
                    appointment_doctor_time__doctor__specialities__name__icontains=query) | Q(
                    appointment_doctor_time__doctor__procedures__name__icontains=query)).distinct()
        if visit_date:
            queryset = queryset.filter(appointment_doctor_time__date=visit_date)
        else:
            queryset = queryset.filter(appointment_doctor_time__date=datetime.datetime.now().date())
        return queryset


class ClientClinicAppointmentsUpdateView(UpdateAPIView):
    model = Appointment
    serializer_class = AppointmentDoctorTimeCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        appointment_id = kwargs['appointment_id']
        appointment = self.model.objects.get(id=appointment_id)
        visited = request.data.get('visited')
        note = request.data.get('note')
        if visited:
            appointment.is_visited = True
        if note:
            appointment.note = note
        appointment.save()

        return Response(status=204)


class ClientClinicTotalReconciliationsView(ListAPIView):
    model = MonthReport
    serializer_class = ClientClinicTotalReconciliationsSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = ClientAdminPagination

    def get_queryset(self):
        address_id = self.kwargs.get('address_id')
        queryset = self.model.objects.filter(
            address__clinic__user=self.request.user,
            address_id=address_id)
        return queryset.order_by('-month')


class ClientClinicTotalReconciliationsDetailView(ListAPIView):
    model = Appointment
    serializer_class = ClientClinicAppointmentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = ClientAdminPagination

    def get_queryset(self):
        date = self.kwargs.get('month')
        address_id = self.kwargs.get('address_id')
        queryset = Appointment.objects.filter(
            appointment_doctor_time__doctor__clinic__user=self.request.user,
            appointment_doctor_time__date__month=date[:2],
            appointment_doctor_time__date__year=date[3:8],
            appointment_doctor_time__clinic_address_id=address_id,
        ).order_by('-created_at')
        query = self.request.GET.get('query')
        visit_date = self.request.GET.get('visit_date')
        if query:
            queryset = queryset.filter(
                Q(appointment_doctor_time__doctor__first_name__icontains=query) | Q(
                    appointment_doctor_time__doctor__last_name__icontains=query) | Q(
                    appointment_doctor_time__doctor__last_name__icontains=query) | Q(
                    appointment_doctor_time__doctor__middle_name__icontains=query) | Q(
                    appointment_doctor_time__doctor__specialities__name__icontains=query) | Q(
                    appointment_doctor_time__doctor__procedures__name__icontains=query)).distinct()
        if visit_date:
            queryset = queryset.filter(appointment_doctor_time__date=visit_date)
        return queryset


class ClientClinicTotalReconciliationsExportView(APIView):
    def get(self, request, *args, **kwargs):
        address = kwargs['address_id']
        date = kwargs['month']
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="export.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Expenses')
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        columns = [
            "Номер", "Пациент", "Телефон пациента", "ИИН пациента", "Доктор", "Услуга",
            "Дата приема"
        ]
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)
        font_style = xlwt.XFStyle()

        counter = 0
        appointments = Appointment.objects.filter(
            appointment_doctor_time__clinic_address=address,
            appointment_doctor_time__date__year=date[3:7],
            appointment_doctor_time__date__month=date[0:2])
        for appointment in appointments:
            row_num += 1
            if appointment.doctor_speciality:
                doctor_service_name = appointment.doctor_speciality.speciality.name
            elif appointment.doctor_procedure:
                doctor_service_name = appointment.doctor_procedure.procedure.name
            else:
                doctor_service_name = ''
            counter += 1
            row = [counter, appointment.patient.first_name, appointment.patient.phone,
                   appointment.patient.iin,
                   '{} {} {}'.format(appointment.appointment_doctor_time.doctor.last_name,
                                     appointment.appointment_doctor_time.doctor.first_name,
                                     appointment.appointment_doctor_time.doctor.middle_name).strip(),
                   doctor_service_name,
                   appointment.appointment_doctor_time.date]
            for col_num in range(len(row)):
                ws.write(row_num, col_num, str(row[col_num]), font_style)
        wb.save(response)
        return response

class ClientClinicProceduresView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = Procedure.objects.all().exclude(parent=None)
        serializer = ProcedureSerializer(queryset, many=True)
        return Response(serializer.data)