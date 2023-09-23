from django.contrib import admin
from .models import Historyquiz,Geographyquiz,Astronomyquiz
from user_profiles.models import profile

admin.site.register(profile)
admin.site.register(Historyquiz)
admin.site.register(Geographyquiz)
admin.site.register(Astronomyquiz)