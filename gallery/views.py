from django.shortcuts import render, redirect
from .models import Image, Picture

# Create your views here.
def home(request):
    context = {
      'images': Image.objects.all(),
      
    }
    
    return render(request,'gallery.html', context)

def photoboom(request):
    return render(request, 'photoboom.html')
    

def lensflare(request):
    
    context = {
      'pictures': Picture.objects.all()
      
    }
    
    return render(request, 'lensflare.html', context)