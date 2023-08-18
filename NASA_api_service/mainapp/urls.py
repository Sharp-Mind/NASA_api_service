from django.urls import path
from mainapp import views


urlpatterns = [
   path ('', views.asteroids_works, name='asteroids_works'),
]