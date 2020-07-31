from django.contrib import admin
from .models import Alarm


class AlarmAdmin(admin.ModelAdmin):
    list_display = ('alarm_time', 'title', 'description')


admin.site.register(Alarm, AlarmAdmin)

# Register your models here.
