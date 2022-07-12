from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from .models import *
from django.shortcuts import render,redirect






def home(request):
    context={}
    return render(request,'home.html',context)




