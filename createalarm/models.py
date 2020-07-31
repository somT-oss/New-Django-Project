from django.db import models


class Alarm(models.Model):
    alarm_time = models.TimeField()
    title = models.CharField(max_length=125, blank=False)
    description = models.CharField(max_length=125, blank=False)



# Create your models here.
