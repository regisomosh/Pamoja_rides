from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.http import JsonResponse
from geopy.distance import geodesic
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class HomeView(TemplateView):
    template_name = 'rider/home.html'

def calculate_distance(request):
    if request.method == 'POST':
        lat = float(request.POST.get('lat'))
        lng = float(request.POST.get('lng'))
        dest_coordinates = (1.3, 36.8)  # Example destination coordinates
        clicked_coordinates = (lat, lng)
        distance = geodesic(clicked_coordinates, dest_coordinates).kilometers
        return JsonResponse({'distance': distance})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)