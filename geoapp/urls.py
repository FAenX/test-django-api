from django.urls import path, include
from .views import find_closest_points_in_grid_payload


urlpatterns = [
    path('distance/', find_closest_points_in_grid_payload), # new
]