from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisment
def index(request):
    advertisment=Advertisment.objects.all()
    context={'advertisment': advertisment}
    return render(request,'index.html', context)

def top_sellers(request):
    return render(request,"top-sellers.html")


