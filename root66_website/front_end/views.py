from django.shortcuts import render

# Create your views here.

def home(request):
    """Home Page for Website"""
    # List of image filenames
    # List of image filenames
    images = ['image1.png', 'image2.png', 'image3.png']

    # Pass the info and images variables to the template
    return render(request, 'front_end/home.html', {'images': images})
    