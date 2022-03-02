from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import *
from .forms import ContactForm
from django.utils.dateparse import parse_date
from home.forms import *
from home.models import *
# Create your views here.
def contact(request):
   
    if request.method == 'POST'and 'save_contact' in request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            saving = form.save()
            messages.success(request,"Thank you ,for your time!!")
            return HttpResponseRedirect('contact')
        else:
            messages.error(request,"please review your form..")
    else:
        form = ContactForm()
    if request.method == 'POST' and 'save_subscribe' in request.POST:
        form1 = SubsriberForm(data=request.POST)
        if form1.is_valid():
            form1.save()
            messages.success(request, 'Successfully subscribed..!')
            return HttpResponseRedirect(request.path_info)
        else:
                messages.error(request, 'Invalid subscription..!')

    else:
        form1 = SubsriberForm()    
    params = {'contact_form':form,'form':form1}
    return render(request, 'contact/contact.html',params)

