from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import *
from home.forms import *
from home.models import *

from django.shortcuts import redirect
import json
import urllib
from django.conf import settings


def BlogsView(request):
    researchs = Blog.objects.all()
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
    params = {'research': researchs,'form':form}
    return render(request,'blogs/blogs.html',params)

def BlogsdetailView(request,tk):
    detailblogs = get_object_or_404(Blog, sno=tk)
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
    params={'details':detailblogs,'form':form} 
    return render(request,'blogs/blogsDetail.html',params)    