from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.contrib import messages
from home.models import *
from home.forms import *
from .models import *
from django.views.generic import ListView
from django.shortcuts import redirect
import json
import urllib
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.conf import settings
from django.template.loader import render_to_string

def SearchView(request):
    ctx = {}
    url_parameter = request.GET.get("q")

    if url_parameter:
        report = Report.objects.filter(Heading__icontains=url_parameter)
    else:
        report = Report.objects.all()

    ctx["report"] = report
    if request.is_ajax():

        html = render_to_string(
            template_name="Resources/searchview.html", context={"report": report}
        )
        data_dict = {"html_from_view": html}
        return JsonResponse(data=data_dict, safe=False)

    return render(request, "Resources/report.html", context=ctx)
def ResourcesView(request):
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
    resource  = Resource.objects.all()
    params = {'resource':resource,'form':form}
    return render(request,'Resources/resources.html',params)

def ReportView(request):
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
    resource  = Report.objects.all()
    params = {'report':resource,'form':form}
    return render(request,'Resources/report.html',params)



def PhotosView(request):
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
    images = Image_multiple.objects.all()
    Videos = Resource_Video.objects.all()
    title = Image_Resource.objects.all()
    params = {'image':images,'Videos':Videos,'title':title,'form':form}
    return render(request, 'Resources/videophotos.html', params)
     
    

def brouchersView(request):
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
    postering = Poster_multiple.objects.all()
    title    =  Poster_Resource.objects.all()
    params = {'posters':postering,'title':title,'form':form}
    return render(request, 'Resources/brouchers.html', params)