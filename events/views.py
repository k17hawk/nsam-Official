from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.http import HttpResponseRedirect

from django.shortcuts import render
from itertools import chain
from .models import *
from home.models import *
from home.forms import *
from django.contrib import messages
from django.shortcuts import redirect
import json
import urllib

from django.conf import settings
# Create your views here.

def EventView(request):
    news =New.objects.all()
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
    params = {'news':news,'form':form}
    return render(request,'NewsAndEvents/newsandEvent.html',params)



def newsdetailView(request,tk):
    detailnews = get_object_or_404(New, id=tk)
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
    params={'details':detailnews,'form':form} 
    return render(request,'NewsAndEvents/newsDetail.html',params)        
