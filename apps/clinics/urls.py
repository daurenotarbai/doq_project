from django.urls import path, include
from rest_framework import routers

from apps.clinics.views import SpecialitiesViewSet, ProceduresViewSet, ClinicsViewSet, MainSearchClinicView, \
    main_for_test

router = routers.DefaultRouter()
router.register(r'specialities', SpecialitiesViewSet)
router.register(r'procedures', ProceduresViewSet)
router.register(r'clinics', ClinicsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('search/<str:query>/', MainSearchClinicView.as_view()),
    path('test/', main_for_test)
]