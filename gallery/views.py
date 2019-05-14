from django.shortcuts import render, redirect
from .models import Image, Picture, Location, Category

# Create your views here.
def home(request):
    context= Image.objects.all()

    locations=Location.get_location()
    return render(request,'gallery.html', {"images":context,'locations':locations})

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

def location(request, locate_id):
    

    try:
        locations=Location.get_location()
        image_url=Image.objects.filter(locate=locate_id)
    except Exception as e:
        raise Http404()
        assert False

    return render(request, 'location.html', {'images': image_url, 'locations': locations})
    
