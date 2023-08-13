from django.shortcuts import render
from rest_framework import generics
from mainapp.forms import *
import NASA_api_service.settings as settings
import requests
import datetime


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


NASA_API_URL = 'https://api.nasa.gov/neo/rest/v1/feed'


def index_page(request):

    content = {1: '1'}

    return render(request, "mainapp/index.html", content)

def asteroid_request_form(request):

    if request.method == 'POST':
        form = AsteroidRequestForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # print(datetime.datetime.now(tz=tz))
    else:
        form = AsteroidRequestForm()

    return render(request, "mainapp/asteroid_request_form.html", {'form': form})

def asteroids_works(request):
    json_data = {}

    if request.method == 'POST':
        form = AsteroidRequestForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            objects_count = form.cleaned_data.get('objects_count')

            if end_date == None:                
                end_date = form.cleaned_data.get('start_date')

            print(form.fields['end_date'])
            
            json_data = {'start_date': start_date, 'end_date': end_date, 'api_key': settings.API_KEY}
            # json_data = {'start_date': '2015-09-07', 'end_date': '2015-09-07', 'api_key': 'qBPba4eivyXWEtU4BWfqlN25IsFBzdWUUDNkr9hh'}
            print('asteroids_list')           
            
            response = requests.get(url=NASA_API_URL, params=json_data)
            answer = response.json()
            # print('answer:', answer['near_earth_objects'].items())

            # print(list(answer['near_earth_objects'])[0])

            asteroids_by_dates = list(answer['near_earth_objects'])
            for date in asteroids_by_dates:
                for asteroid in answer['near_earth_objects'][date]:
                    # TODO: сделать вывод первых нескольких записей
                    print(asteroid['name'])
                    print(asteroid['absolute_magnitude_h'])
                    print(asteroid['is_potentially_hazardous_asteroid']) 
                                       
                # print(answer['near_earth_objects'][date])
            # asteroids_groups_list = answer
            context = {'form': form, 'asteroids_groups_list': dict(answer), 'dates': dates}

            
            # print(datetime.datetime.now(tz=tz))
    else:
        form = AsteroidRequestForm()
        context = {'form': form}

    
    # for i in range(len(answer['near_earth_objects'][date_field])):
        # print(answer['near_earth_objects'][date_field][i]['is_potentially_hazardous_asteroid'])

    return render(request, "mainapp/asteroids.html", context)