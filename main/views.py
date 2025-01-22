from django.shortcuts import render
from .models import ProfileModel

# Create your views here.

def Homepagview(request):
     models = ProfileModel
     return render