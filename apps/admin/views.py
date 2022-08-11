from rest_framework.generics import ListAPIView

from apps.admin.serializers import ClientClinicDoctorsSerializer, ClientClinicFeedbacksSerializer
from apps.clinics.models import Doctor, Clinic
from apps.patients.models import Comment


class ClientClinicDoctorsView(ListAPIView):
    model = Doctor
    serializer_class = ClientClinicDoctorsSerializer

    def get_queryset(self):
        clinic_id = Clinic.objects.filter(user=self.request.user).first()
        queryset = self.model.objects.filter(clinic=clinic_id)
        return queryset


class ClientClinicFeedbacksView(ListAPIView):
    model = Comment
    serializer_class = ClientClinicFeedbacksSerializer

    def get_queryset(self):
        queryset = Comment.objects.filter(doctor__clinic__user=self.request.user, parent=None)
        return queryset
