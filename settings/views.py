from django.shortcuts import render
from .models import About
# Create your views here.

def about(request):
    object = About.objects.all()
    return render(request,'settings/about.html',{'abouts':object})