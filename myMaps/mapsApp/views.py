from django.shortcuts import render, HttpResponse, redirect
from dotenv import load_dotenv
import os
from users.models import Route
import json
import requests


# Create your views here.
def maps(request):
    print(request.session.get("username"))
    routes = Route.objects.filter(user_id=request.session.get("username"))
    routes_json = json.dumps([route.to_dict() for route in routes])
    return render(request, "maps.html",{"routes_json": routes_json, "routes":routes})

def mapsKey(request):
    load_dotenv()
    return HttpResponse(os.environ.get("MAPBOX_TOKEN"))

def getDirections(request, modeOfTransport, startLong, startLat, endLong, endLat):
    # `https://api.mapbox.com/Directions/v5/mapbox/${modeOfTransport}/${path.startPoint.long},${path.startPoint.lat};${path.endPoint.long},${path.endPoint.lat}?geometries=geojson&access_token=${mapboxToken}`
    load_dotenv()
    print(modeOfTransport)
    token = os.environ.get("MAPBOX_TOKEN")
    response = requests.get(f"https://api.mapbox.com/directions/v5/mapbox/cycling/{startLong},{startLat};{endLong},{endLat}?geometries=geojson&access_token={token}")
    return HttpResponse(response)

def createRoute(request):
    if request.method == "POST":
        print(request.session.get("username"))
        startLong = request.POST.get('start_long')
        startLat = request.POST.get('start_lat')
        endLong = request.POST.get('end_long')
        endLat = request.POST.get('end_lat')
        print(startLat,startLong,endLat,endLong)

        # newRoute = Route(user_id=request.session.get("username"), routeName="Route4", startPoint={"lat":34.686647, "long": 32.005162}, endPoint={"lat":34.875084, "long": 32.736881})
        # newRoute.save()
        return redirect("maps")