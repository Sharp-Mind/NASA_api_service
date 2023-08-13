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
    path ('asteroids.html', views.asteroids_works, name='asteroids_works'),
    # path ('get_asteroids.html', views.get_asteroids, name='get_asteroids'),
]