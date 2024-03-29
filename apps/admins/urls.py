from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from apps.admins.views import ClientClinicDoctorsView, ClientClinicFeedbacksView, \
    ClientClinicAppointmentsView, ClientClinicDoctorsAppointmentTimesView, \
    ClientClinicDoctorsAppointmentTimesCreateView, ClientClinicAppointmentTimesView, \
    ClientClinicReconciliationsView, ClientClinicAppointmentsUpdateView, \
    ClientClinicTotalReconciliationsView, ClientClinicDoctorsDetailView, ClientClinicAddressView, \
    ClientClinicDoctorsSpecialityCreateView, ClientClinicDoctorsProcedureCreateView, \
    ClientClinicDoctorsSpecialitiesUpdateView, ClientClinicDoctorsProceduresUpdateView, \
    ClientClinicFeedbacksDetailView, ClientClinicTotalReconciliationsDetailView, \
    ClientClinicTotalReconciliationsExportView, ClientClinicProceduresView

urlpatterns = [
    path('appointment-times/doctor/<int:doctor_id>/address/<int:address_id>', ClientClinicAppointmentTimesView.as_view()),
    path('addresses', ClientClinicAddressView.as_view()),

    path('doctor-appointment-times/address/<int:address_id>',
         ClientClinicDoctorsAppointmentTimesView.as_view()),
    path('doctor-appointment-times/doctors/<int:doctor_id>',
         ClientClinicDoctorsAppointmentTimesCreateView.as_view()),

    path('appointments', ClientClinicAppointmentsView.as_view()),
    path('procedures', ClientClinicProceduresView.as_view()),
    path('appointments/<int:appointment_id>/update', ClientClinicAppointmentsUpdateView.as_view()),
    path('reconciliations', ClientClinicReconciliationsView.as_view()),
    path('total-reconciliations/<int:address_id>', ClientClinicTotalReconciliationsView.as_view()),
    path('total-reconciliations/<int:address_id>/month/<str:month>',
         ClientClinicTotalReconciliationsDetailView.as_view()),
    path('total-reconciliations/<int:address_id>/month/<str:month>/export',
         ClientClinicTotalReconciliationsExportView.as_view()),
    path('feedbacks', ClientClinicFeedbacksView.as_view()),
    path('feedbacks/<int:id>', ClientClinicFeedbacksDetailView.as_view()),
    path('doctors/address/<int:address_id>', ClientClinicDoctorsView.as_view()),
    path('doctors/<int:doctor_id>/address/<int:address_id>',
         ClientClinicDoctorsDetailView.as_view()),
    path('doctors/specialities', ClientClinicDoctorsSpecialityCreateView.as_view()),
    path('doctors/specialities/<int:id>', ClientClinicDoctorsSpecialitiesUpdateView.as_view()),
    path('doctors/procedures', ClientClinicDoctorsProcedureCreateView.as_view()),
    path('doctors/procedures/<int:id>', ClientClinicDoctorsProceduresUpdateView.as_view()),

]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
