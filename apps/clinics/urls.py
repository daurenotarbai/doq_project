from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from apps.clinics.views import SpecialitiesView, ProceduresView, ClinicsViewSet, \
    MainSearchClinicView, \
    DoctorAppointmentTimesView, ClinicDoctorsView, DoctorsDetailView, \
    DoctorCommentsView, \
    ProcedureDoctorsView, SpecialityDoctorsView, ClinicCommentsView, SpecialitiesDetailView, \
    ProceduresDetailView, ClinicApplicationCreateView

router = routers.DefaultRouter()
router.register(r'clinics', ClinicsViewSet, 'clinic_list')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('create/application', ClinicApplicationCreateView.as_view()),

    path('search/<str:query>/', MainSearchClinicView.as_view()),

    path('clinics/<int:clinic_id>/doctors', ClinicDoctorsView.as_view()),
    path('clinics/<int:clinic_id>/comments', ClinicCommentsView.as_view()),

    path('procedures/', ProceduresView.as_view()),
    path('procedures/<int:pk>/', ProceduresDetailView.as_view()),

    path('specialities/', SpecialitiesView.as_view()),
    path('specialities/<int:pk>/', SpecialitiesDetailView.as_view()),

    path('procedures/<int:procedure_id>/doctors', ProcedureDoctorsView.as_view()),
    path('specialities/<int:speciality_id>/doctors', SpecialityDoctorsView.as_view()),

    path('doctors/<int:doctor_id>/address/<int:address_id>/appointments',
         DoctorAppointmentTimesView.as_view()),
    path('doctors/<int:pk>/', DoctorsDetailView.as_view()),
    path('doctors/<int:doctor_id>/comments', DoctorCommentsView.as_view()),

]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
