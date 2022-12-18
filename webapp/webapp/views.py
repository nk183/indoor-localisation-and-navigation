from django.shortcuts import render
# from user.models import *
from .utils import get_plot

def home(request):
    return render(request,'landingpage.html')

def locate(request):
    x = [1,2,3,4]
    y = [1,2,3,4]
    chart = get_plot(x,y)
    return render(request,'locatePage.html',{'chart':chart})