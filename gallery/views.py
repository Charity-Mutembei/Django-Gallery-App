from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Image, Category, Location
from .forms import ImageForm
# Create your views here.
def welcome (request):
    '''
    this is the landing page. Containns the home page of this application
    '''
    return render (request, 'landing.html')

def image (request):
    try: 
        images = Image.objects.all()
        categories = Category.objects.all()
        locations = Location.objects.all()
        context = {'categories': categories, 'locations': locations, 'images': images}
    
    except ValueError:
        raise Http404()
    
    return render(request, 'landing.html', context)

def updateImage(request, pk):
    '''
    this is a method that allows us to update images
    '''
    image = Image.objects.get(id = pk)
    categories = Category.objects.all()
    locations = Location.objects.all()
    context = {'categories': categories, 'locations': locations}
    form = ImageForm(instance = image)

    if request.method == 'POST':
        form = ImageForm(request.POST, instance = image)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'image_form.html', context)


def deleteImage(request, pk):
    '''
    method that will delete images 
    '''
    image = Image.objects.get(id = pk)
    
    if request.method == 'POST':
        image.delete()
        return redirect('home')
    
    return render(request, 'delete.html', {'obj': image})


