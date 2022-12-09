from django.shortcuts import render

# Create your views here.
from .models import *


def index(request):
    return render(request, 'shareimp/index.html', {'title':'Добро пожаловать | Places Remember '})


def user_page(request):
    posts = Place.objects.all()
    return render(request, 'shareimp/userpage.html', {'posts':posts})

