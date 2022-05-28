from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome (request):
    '''
    this is the landing page. Containns the home page of this application
    '''
    return render (request, 'landing.html')
