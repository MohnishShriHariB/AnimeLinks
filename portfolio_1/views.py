from django.shortcuts import render
from django.http import HttpResponse
from portfolio_1.models import project

def home(request):
    projects=project.objects.all()
    return render(request,'portfolio_1/home.html',{'projects':projects})
