from rest_framework import permissions
from rest_framework.generics import ListAPIView

from apps.admin.serializers import ClientClinicDoctorsSerializer, ClientClinicFeedbacksSerializer, \
    ClientClinicAppointmentSerializer
from apps.clinics.models import Doctor, Clinic
from apps.patients.models import Comment, Appointment


class ClientClinicDoctorsView(ListAPIView):
    model = Doctor
    serializer_class = ClientClinicDoctorsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        clinic_id = Clinic.objects.filter(user=self.request.user).first()
        queryset = self.model.objects.filter(clinic=clinic_id)
        return queryset


class ClientClinicFeedbacksView(ListAPIView):
    model = Comment
    serializer_class = ClientClinicFeedbacksSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        queryset = Comment.objects.filter(doctor__clinic__user=self.request.user, parent=None)
        return queryset


class ClientClinicAppointmentsView(ListAPIView):
    model = Appointment
    serializer_class = ClientClinicAppointmentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        queryset = Appointment.objects.filter(
            appointment_doctor_time__doctor__clinic__user=self.request.user)
        return queryset
