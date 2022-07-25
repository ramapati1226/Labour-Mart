

from django.shortcuts import render
from .models import labour_detail
from math import ceil

# Create your views here.
from django.http import HttpResponse

def index(request):
    products = labour_detail.objects.all()
    print(products)
    return render(request,"labour/index.html")

def about(request):

    return render(request,"labour/about.html")

def contact(request):
    return render(request,"labour/contact.html")

def login(request):
    return render(request,"labour/login.html")

def search(request):
    return render(request,"labour/search.html")

def privacy(request):
    return render(request,"labour/privacy.html")

def jobs(request):
    return render(request,"labour/jobs.html")
def services(request):
    return render(request,"labour/services.html")

