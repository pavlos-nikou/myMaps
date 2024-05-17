from django.shortcuts import render, HttpResponse, redirect
from dotenv import load_dotenv
import os
from users.models import Route
import json
import requests


# Create your views here.
def maps(request):
    alert = None
    if request.session.get("alert"):
        alert = request.session.get("alert")
        request.session["alert"] = None
    print(request.session.get("alert"))
    if request.session.get("username") == None:
        request.session["alert"] = "You have to be Signed In to access the Maps!!!"
        # request.session["alert"] = None
        return redirect("/signIn")
    print(request.session.get("username"))
    routes = Route.objects.filter(user_id=request.session.get("username"))
    routes_json = json.dumps([route.to_dict() for route in routes])
    return render(request, "maps.html",{"routes_json": routes_json, "routes":routes, "alert": alert})

def mapsKey(request):
    load_dotenv()
    return HttpResponse(os.environ.get("MAPBOX_TOKEN"))

def getDirections(request, modeOfTransport, startLong, startLat, endLong, endLat):
    load_dotenv()
    print(modeOfTransport)
    token = os.environ.get("MAPBOX_TOKEN")
    response = requests.get(f"https://api.mapbox.com/directions/v5/mapbox/cycling/{startLong},{startLat};{endLong},{endLat}?geometries=geojson&access_token={token}")
    return HttpResponse(response)

def createRoute(request):
    if request.method == "POST":
        routeName = request.POST.get("route_name")
        startLong = request.POST.get('start_long')
        startLat = request.POST.get('start_lat')
        endLong = request.POST.get('end_long')
        endLat = request.POST.get('end_lat')
        
        newRoute = Route(user_id=request.session.get("username"), routeName=routeName, startPoint={"lat":startLat, "long": startLong}, endPoint={"lat":endLat, "long": endLong})
        newRoute.save()
        return redirect("maps")

def deleteRoute(request):
    if request.method == "POST":
        routeName = request.POST.get("route_name")
        if Route.objects.filter(routeName=routeName).exists():
            Route.objects.filter(routeName=routeName).delete()
    return redirect("maps")