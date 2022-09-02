from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from apps.clinics.views import SpecialitiesView, ProceduresView, ClinicsView, \
    MainSearchClinicView, \
    DoctorAppointmentTimesView, ClinicDoctorsView, DoctorsDetailView, \
    DoctorCommentsView, \
    ProcedureDoctorsView, SpecialityDoctorsView, ClinicCommentsView, SpecialitiesDetailView, \
    ProceduresDetailView, ClinicApplicationCreateView, CityView, ClinicsDetailView, \
    ProceduresListView, SpecialitiesListView

router = routers.DefaultRouter()
# router.register(r'^city/{city_id}/clinics', ClinicsViewSet, 'clinic_list')

urlpatterns = [
    path('', include(router.urls)),
    path('cities', CityView.as_view()),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('city/<int:city_id>/clinics/', ClinicsView.as_view()),
    path('city/<int:city_id>/clinics/<int:pk>', ClinicsDetailView.as_view()),

    path('create/application', ClinicApplicationCreateView.as_view()),

    path('search/<str:query>/', MainSearchClinicView.as_view()),

    path('clinics/<int:clinic_id>/doctors', ClinicDoctorsView.as_view()),
    path('clinics/<int:clinic_id>/comments', ClinicCommentsView.as_view()),

    path('city/<int:city_id>/procedures/', ProceduresView.as_view()),
    path('city/<int:city_id>/procedures/<int:pk>/', ProceduresDetailView.as_view()),

    path('city/<int:city_id>/specialities/', SpecialitiesView.as_view()),
    path('city/<int:city_id>/specialities/<int:pk>/', SpecialitiesDetailView.as_view()),

    path('specialities/', SpecialitiesListView.as_view()),
    path('procedures/', ProceduresListView.as_view()),

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
