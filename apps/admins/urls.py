from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from apps.admins.views import ClientClinicDoctorsView, ClientClinicFeedbacksView, \
    ClientClinicAppointmentsView, ClientClinicDoctorsAppointmentTimesView, \
    ClientClinicDoctorsAppointmentTimesCreateView, ClientClinicAppointmentTimesView, \
    ClientClinicReconciliationsView, ClientClinicAppointmentsUpdateView, \
    ClientClinicTotalReconciliationsView, ClientClinicDoctorsDetailView, ClientClinicAddressView

urlpatterns = [
    path('appointment-times', ClientClinicAppointmentTimesView.as_view()),
    path('addresses', ClientClinicAddressView.as_view()),

    path('doctor-appointment-times/address/<int:address_id>',
         ClientClinicDoctorsAppointmentTimesView.as_view()),
    path('doctor-appointment-times/doctors/<int:doctor_id>',
         ClientClinicDoctorsAppointmentTimesCreateView.as_view()),

    path('appointments', ClientClinicAppointmentsView.as_view()),
    path('appointments/<int:appointment_id>/update', ClientClinicAppointmentsUpdateView.as_view()),
    path('reconciliations', ClientClinicReconciliationsView.as_view()),
    path('total-reconciliations/<int:address_id>', ClientClinicTotalReconciliationsView.as_view()),
    path('feedbacks', ClientClinicFeedbacksView.as_view()),
    path('doctors', ClientClinicDoctorsView.as_view()),
    path('doctors/<int:id>', ClientClinicDoctorsDetailView.as_view()),

]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
