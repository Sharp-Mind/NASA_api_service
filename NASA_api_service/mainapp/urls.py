from django.urls import path
from mainapp import views

urlpatterns = [
    # path(
    #     "api/v1/asteroids",
    #     views.AsteroidsListAPIView.as_view(),
    #     name="asteroids",
    # ),
    # path(
    #     "api/v1/calculations/<str:cid>",
    #     views.SingleCalculationListAPIView.as_view(),
    #     name="single_calculation",
    # ),

    # path(
    #     "api/v1/asteroids",
    #     views.asteroids,
    #     name="asteroids",
    # ),

    path ('', views.index_page, name='index_page'),
    path ('asteroid_request_form.html', views.asteroid_request_form, name='asteroid_request_form'),
    path ('get_asteroids.html', views.get_asteroids, name='get_asteroids'),
]