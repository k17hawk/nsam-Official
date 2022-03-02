from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.contrib import messages
from home.models import *
from home.forms import *
from .models import *
from django.shortcuts import redirect
import json
import urllib
from django.conf import settings


def ProjectsView(request):
    ongoing = Ongoing.objects.all()
    completed = Completed.objects.all()
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
    params = {'completed':completed,'ongoing':ongoing,'form':form}
    return render(request,'Projects/projects.html',params)

def OngoingView(request):
    ongoing = Ongoing.objects.all()
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
  
    params = {'ongoing':ongoing,'form':form}
    return render(request,'Projects/ongoing.html',params)

def CompletedView(request):
    completed = Completed.objects.all()
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
  
    params = {'completed':completed,'form':form}
    return render(request,'Projects/completed.html',params)   

def detailcompletedview(request,pk):
    detailCompleted = get_object_or_404(Completed, Id=pk)
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
   
    params={'details':detailCompleted,'form':form}
    return render(request,'Projects/DetailCompleted.html',params)        

def detailongoingview(request,sk):
    ongoingCompleted = get_object_or_404(Ongoing, Id=sk)
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
    params={'details':ongoingCompleted,'form':form}
    return render(request,'Projects/DetailOngoing.html',params)      