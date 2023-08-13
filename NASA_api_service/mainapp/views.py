from django.shortcuts import render
from rest_framework import generics
from mainapp.forms import *
import requests


# class AsteroidsListAPIView(generics.ListAPIView):
#     def get(self, request, *args, **kwargs):

#         nasa_data = requests.get('https://api.nasa.gov/neo/rest/v1/feed')
#         print(nasa_data)

#         return super().get(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):       

#         return super().get(request, *args, **kwargs)

# def asteroids(request):
#     if request.method == "GET":
#         nasa_data = requests.get('https://api.nasa.gov/neo/rest/v1/feed', headers={'api_key': 'DEMO_KEY'})
#         print(nasa_data)
#     elif request.method == "POST":
#         pass

def index_page(request):

    content = {1: '1'}

    return render(request, "mainapp/index.html", content)

def asteroid_request_form(request):

    if request.method == 'POST':
        form = AsteroidRequestForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = AsteroidRequestForm()

    return render(request, "mainapp/asteroid_request_form.html", {'form': form})

def get_asteroids(request):
    response = requests.get('https://sky.pro/media/')
    print(response.ok)
    print(response.text)