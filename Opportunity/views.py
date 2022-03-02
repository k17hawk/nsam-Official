from django.shortcuts import render
from .models import *
from home.models import *
from home.forms import *
from django.contrib import messages
# Create your views here.
def OppoViews(request):
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
    params = {'form':form}       
    return render(request,'Opportunity/Opportunity.html',params)

def InternViews(request):
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
    params = {'form':form}        
    return render(request,'Opportunity/internship.html',params)

def VolunterViews(request):
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
    params = {'form':form}    
    return render(request,'Opportunity/volunter.html',params)        