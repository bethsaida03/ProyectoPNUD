from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView 
from django.template import loader

# Create your views here.
# class Home(ListView): 
#     #para la vista 'home'
#     template_name = 'SitioWeb/home.html'
def Home(request):
    return render(request, 'SitioWeb/home.html', {})