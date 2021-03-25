
from django.contrib import admin
from .models import Analytics
# Register your models here.

class AnalyticsAdmin(admin.ModelAdmin):
    list_display = ('name', 'competen', 'teach','punc','prac','approach','classcontrol' )

admin.site.register(Analytics, AnalyticsAdmin)