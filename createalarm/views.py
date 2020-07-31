from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Alarm
from .forms import AlarmForm


def home_view(request):
    return render(request, 'homeview.html')



def create_alarm_view(request):
    my_form = AlarmForm()
    if request.method == "POST":
        my_form = AlarmForm(request.POST)
        if my_form.is_valid():
            my_form.save()
            return HttpResponseRedirect('/newalarm/')

    # if request.method == "POST":
    #     if my_form.is_valid():
    #         Alarm.objects.create(**my_form.cleaned_data)
    #     else:
    #         print(my_form.errors)
    #
    context = {"form": my_form}
    return render(request, 'createalarm.html', context)


def new_alarm(request):
    obj = Alarm.objects.all()
    context = {
        "object": obj,
    }
    return render(request, 'newalarm.html', context)
# Create your views here.
