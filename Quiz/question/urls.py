from django.urls import path
from . import views
from .views import HistoryListView,GeographyListView,AstronomyListView,HistoryCreateView,GeographyCreateView,AstronomyCreateView
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.intro,name="intro"),
    path('log_in/',views.log_in,name="log-in"),
    path('log_out/',auth_view.LogoutView.as_view(template_name="log_out.html"),name="log-out"),
    path('register/',views.sign_up,name="sign-up"),
    path('category/',views.category,name="category"),
    path('history_quiz/intro/',views.history_intro,name="history-intro"),
    path('geography_quiz/intro/',views.geography_intro,name="geography-intro"),
    path('astronomy_quiz/intro/',views.astronomy_intro,name="astronomy-intro"),

    path('history_quiz',HistoryListView.as_view(),name="history"),
    path('history_quiz/finished/',views.history_finished,name='history-finished'),
    path('history_quiz/create/',HistoryCreateView.as_view(),name="history-create"),

    path('geography_quiz',GeographyListView.as_view(),name="geography"),
    path('geography_quiz/finished/',views.geography_finished,name='geography-finished'),
    path('geography_quiz/create/',GeographyCreateView.as_view(),name="geography-create"),

    path('astronomy_quiz',AstronomyListView.as_view(),name="astronomy"),
    path('astronomy_quiz/finished/',views.astronomy_finished,name='astronomy-finished'),
    path('astronomy_quiz/create/',AstronomyCreateView.as_view(),name="astronomy-create"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)