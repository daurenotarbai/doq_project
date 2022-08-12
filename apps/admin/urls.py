from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from apps.admin.views import ClientClinicDoctorsView, ClientClinicFeedbacksView, \
    ClientClinicAppointmentsView

urlpatterns = [
    path('doctors', ClientClinicDoctorsView.as_view()),
    path('feedbacks', ClientClinicFeedbacksView.as_view()),
    path('appointments', ClientClinicAppointmentsView.as_view()),
    # path('doctor-appointment-times', ClientClinicDoctorsAppointmentTimesView.as_view()),

]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
