from audioop import maxpp
from webbrowser import get
from django.db import models
from django.http import Http404

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length= 50)
    def __str__(self):
        return self.name
    def save_location(self):
        self.save()
class Category(models.Model):
    name = models.CharField(max_length= 50)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()
class Image(models.Model):
   
    name =models.CharField(max_length= 100)
    description = models.TextField()
    location = models.ManyToManyField(Location)
    category = models.ManyToManyField(Category)
    image_photo = models.ImageField(upload_to = 'galleries/galleries',default ='')

    def __str__(self):
        return self.name

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
        


