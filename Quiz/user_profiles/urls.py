from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.profile,name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)