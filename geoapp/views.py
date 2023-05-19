import json
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import math
# import django json response
from django.http import JsonResponse

from .models import Grid

# Create your views here.

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def find_closest_points_in_grid(points):
    """
    Find the closest points in a grid to a given point.
    example 2,2;-1,30;20,11;4,5 should return 2,2;4,5
    """

    split_by_semi_colon = points.split(';')
    grid = [(int(i), int(j)) for i, j in [x.split(',') for x in split_by_semi_colon]]

 

    closest_points = []
    min_distance = float('inf')

    for i in range(len(grid)):
        for j in range(i + 1, len(grid)):
            distance = calculate_distance(grid[i], grid[j])
            if distance < min_distance:
                min_distance = distance
                closest_points = [grid[i], grid[j]]
            elif distance == min_distance:
                closest_points.extend([grid[i], grid[j]])\
                
    return closest_points


def error_handler(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return JsonResponse({"error": str(e)})
    return inner



@csrf_exempt
@require_http_methods(["POST"])
@error_handler
def find_closest_points_in_grid_payload(request):
    try:

        payload = json.loads(request.body)
        points = payload["points"]

        
        
        
        closest_points = find_closest_points_in_grid(points)

        # save grid to db

        grid = Grid(points=points, closest_points=closest_points)
        grid.save()


        return JsonResponse(json.dumps({"closest_points": closest_points}), safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)})









