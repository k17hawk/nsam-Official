from django.shortcuts import render
from .models import *
from math import ceil
from home.forms import *
from home.models import *
# Create your views here.
def aboutViews(request):
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
    return render(request, 'about/about.html',params)  


def TeamViews(request):
    allTeams = []
    typeTeam = OurTeam.objects.values('TypeOfMember')
    types = {item['TypeOfMember'] for item in typeTeam}
    for type in types:
        team = OurTeam.objects.filter(TypeOfMember=type)
        n = len(team)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allTeams.append([team,range(1, nSlides), nSlides])
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
   
    params = {'allProds':allTeams,'form':form}
    return render(request, 'about/ourTeam.html',params)  

def AdvisorViews(request):
    advisor = Advisor.objects.all()
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
    params = {'advisors':advisor,'form':form}
    return render(request, 'about/ourAdvisor.html',params)  

def PartnerViews(request):
    donars = Image_multiple_Donar.objects.all()
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
    params={'donars':donars,'form':form}
    return render(request, 'about/ourPartners.html',params)  


