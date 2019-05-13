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

def search_results(request):

    if 'image_name' in request.GET and request.GET["image_name"]:
        search_term = request.GET.get("image_name")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})