from django.shortcuts import render

# Create your views here.

def index(request):
    """Home Page for Website"""
    return render(request, "front_end/index.html")