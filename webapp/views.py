from django.shortcuts import render

def index(request) :
    return render(request,'../templates/webapp/home.html')

# Create your views here.
