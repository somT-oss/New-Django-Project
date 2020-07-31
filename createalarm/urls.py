from django.urls import path
from . import views

urlpatterns = [
    path("", views.create_alarm_view),
    path('new/', views.new_alarm)
]