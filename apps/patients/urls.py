from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from apps.patients.views import CreatePatientAppointmentView, CreateCommentView

urlpatterns = [

    path('make/appointment',
         CreatePatientAppointmentView.as_view()),
    path('leave/comment',
         CreateCommentView.as_view()),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
