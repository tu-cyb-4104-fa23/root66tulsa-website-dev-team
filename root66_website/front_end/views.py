from django.shortcuts import render

# Create your views here.

def home(request):
    """Home Page for Website"""
    return render(request, "front_end/home.html")