from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.http import HttpResponseRedirect
from home.models import *
from home.forms import *
from django.contrib import messages

from django.shortcuts import render


from .models import *

# Create your views here.
def Publichealth(request):
    if request.method == 'POST':
        form = SubsriberForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully subscribed..!')
            return redirect(request.path_info)
        else:
                messages.error(request, 'Invalid subscription..!')

    else:
        form = SubsriberForm()
    health = PublicHealth.objects.all().order_by("-date_And_time")
    params = {'healths':health,'form':form}
    return render(request,'Programmes/publicHealth.html',params)

def AwarnessView(request):
    if request.method == 'POST':
        form = SubsriberForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully subscribed..!')
            return redirect(request.path_info)
        else:
                messages.error(request, 'Invalid subscription..!')

    else:
        form = SubsriberForm()
    awarness = EducationAwarness.objects.all().order_by("-date_And_time")
    params = {'aware':awarness,'form':form}
    return render(request,'Programmes/Awarness.html',params)

def WorkshopView(request):
    if request.method == 'POST':
        form = SubsriberForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully subscribed..!')
            return redirect(request.path_info)
        else:
                messages.error(request, 'Invalid subscription..!')

    else:
        form = SubsriberForm()
    workshop = Workshop.objects.all().order_by("-date_And_time")
    params = {'workshop':workshop,'form':form}
    return render(request,'Programmes/workshop.html',params)

def WildView(request):
    if request.method == 'POST':
        form = SubsriberForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully subscribed..!')
            return redirect(request.path_info)
        else:
                messages.error(request, 'Invalid subscription..!')

    else:
        form = SubsriberForm()
    wildife = wildlife.objects.all().order_by("-date_And_time")
    params = {'wildlife':wildife,'form':form}
    return render(request,'Programmes/wildlife.html',params)
