from django.test import TestCase
from .models import Location, Category, Image

# Create your tests here.

class LocationTestClass(TestCase):
    '''
    class that tests of the class model location
    '''
    #setup method
    def setUp(self):
        self.name = Location(name = '')

    #testing whether we are being instantiated properly

    def test_instance (self):
        self.assertTrue(isinstance(self.name, Location))

    #testing the save method
    def test_save_method(self):
        self.name.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)> 0)
    
class ImageTestClass(TestCase):
    '''
    test the class model image to ensure the application runs properly
    '''