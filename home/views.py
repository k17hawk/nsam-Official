from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from Blogs.models import *
from events.models import *
from .models import *
from About.models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect
import json
import urllib
from django.conf import settings


def home(request):
    slideimage = SlideImage.objects.values()
    blogs = Blog.objects.filter(active=True)
    news = New.objects.filter(active=True)
    donars =Image_multiple_Donar.objects.filter(active=True)
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
    params = {'slideimage':slideimage,'blogs':blogs,'news':news,'donars':donars,'form': form}
    return render(request, 'home/home.html',params)