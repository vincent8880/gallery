from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Image, Location, Category

# Create your views here.
def index(request):
    title = 'Home'
    images = Image.get_all_images()
    locations = Location.objects.all()
    category = Category.objects.all()
    return render(request, 'index.html', {'title':title, 'images':images, 'locations':locations,'category':category})

def single_image(request, category_name, image_id):
    # print(image_category)
    locations = Location.objects.all()

    image = Image.get_image_by_id(image_id)
    # Get category name
    # print(category_name)
    image_category = Image.objects.filter(category__photo_category = category_name)
    title = f'{category_name}'
    return render(request,'single_image.html',{'title':title, 'image':image, 'image_category':image_category, 'locations':locations})

def location_filter(request, location):
    locations = Location.objects.all()
    images = Image.filter_by_location(location)
    title = f'{location} Photos'
    return render(request, 'location.html', {'title':title, 'images':images, 'locations':locations})

def search(request):
    if "term" in request.GET and request.GET["term"]:
        term = request.GET.get("term")
        photos = Image.search_image(term)
        if photos != "No images found":
            message = "Photos of '" + term + "'"
            return render(request, "search.html", {"images":photos,"message":message,"title":term.capitalize()})
        else:
            message = "No images found"
            return render(request, "search.html", {"images":[],"message":message,"title":term.capitalize()})
    