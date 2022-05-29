from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Image, Category, Location
from .forms import ImageForm
from django.db.models import Q

# Create your views here.
def welcome (request):
    '''
    this is the landing page. Containns the home page of this application
    '''
    images = Image.objects.all()
    categories = Category.objects.all()
    locations = Location.objects.all()
    context = {'categories': categories, 'locations': locations, 'images': images}
    return render (request, 'landing.html', context)

def photo (request):
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

def search_results(request):
    call = request.GET.get('q') if request.GET.get('call') != None else ''
    
    images = Image.objects.filter(
        Q(name__icontains = call) |
        Q(category__name__icontains=call) |
        Q(description__icontains=call) |
        Q(location__name__icontains=call)

    )

    locations = Location.objects.all()

    context = {'images': images, 'locations': locations}
    return render(request, 'search.html', context)


