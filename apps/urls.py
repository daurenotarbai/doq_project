from django.urls import include, path

urlpatterns = [
    path("", include("apps.clinics.urls")),
    path("patients/", include("apps.patients.urls")),
]
