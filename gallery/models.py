from audioop import maxpp
from webbrowser import get
from django.db import models
from django.http import Http404

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length= 50)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length= 50)

    def __str__(self):
        return self.name

class Image(models.Model):
    image_photo = models.ImageField(upload_to = 'galleries', null = False, blank = False, default ='media/articles/car3')
    name =models.CharField(max_length= 100)
    description = models.TextField()
    location = models.ForeignKey('Location', on_delete=models.DO_NOTHING)
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING)

    def save_image(self):
        '''
        method to save the image
        '''
        self.save()
    
    @classmethod
    def search_by_category(cls, search_term):
        '''
        method to search image by its category
        '''
        image = cls.objects.filter(category__icontains = search_term)
        return image
    @classmethod
    def filter_by_location(cls, search_term):
        '''
        method to filter images by their location
        '''
        image = cls.objects.filter(location__icontains = search_term)
        return image                           
        


