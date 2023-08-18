from django.shortcuts import render
from mainapp.forms import *
import NASA_api_service.settings as settings
import requests


NASA_API_URL = 'https://api.nasa.gov/neo/rest/v1/feed'

def asteroids_works(request):    
    json_data, asteroids_list = {}, []

    if request.method == 'POST':

        form = AsteroidRequestForm(request.POST)

        if form.is_valid():         
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            objects_count = form.cleaned_data.get('objects_count')

            if end_date == None:                
                end_date = form.cleaned_data.get('start_date')
               
            json_data = {'start_date': start_date, 'end_date': end_date, 'api_key': settings.API_KEY}
            response = requests.get(url=NASA_API_URL, params=json_data)            
            answer = response.json()        
            asteroids_by_dates = list(answer['near_earth_objects'])
        
            def get_asteroid():
                for date in asteroids_by_dates:                
                    for asteroid in answer['near_earth_objects'][date]:                  
                        yield {'date': date, 'name': asteroid['name'], 'absolute_magnitude_h': asteroid['absolute_magnitude_h'], 'is_hazardous': asteroid['is_potentially_hazardous_asteroid']}        

            asteroid = get_asteroid()

            for _ in range(objects_count):                
                asteroids_list.append(next(asteroid))           
            context = {'form': form, 'asteroids': asteroids_list}                      
            
    else:
        form = AsteroidRequestForm()
        context = {'form': form}

    return render(request, "mainapp/index.html", context)
