from django.shortcuts import render, HttpResponse, redirect
from dotenv import load_dotenv
import os
from users.models import Route
import json
import requests

# load maps voew
def maps(request):
    # handle alerts on the page
    alert = None
    if request.session.get("alert"):
        alert = request.session.get("alert")
        request.session["alert"] = None
    # check if user is singed in if not redirect to sign in and send an alert
    if request.session.get("username") == None:
        request.session["alert"] = "You have to be Signed In to access the Maps!!!"
        # request.session["alert"] = None
        return redirect("/signIn")
    # get the routes of the signed in user
    routes = Route.objects.filter(user_id=request.session.get("username"))
    routes_json = json.dumps([route.to_dict() for route in routes])
    # render the map with the users routes and any alerts if they exist
    return render(request, "maps.html",{"routes_json": routes_json, "routes":routes, "alert": alert})

# return the mapbox token
def mapsKey(request):
    load_dotenv()
    return HttpResponse(os.environ.get("MAPBOX_TOKEN"))

# returns direction for the route the user wants to display on the map
def getDirections(request, modeOfTransport, startLong, startLat, endLong, endLat):
    load_dotenv()
    print(modeOfTransport)
    token = os.environ.get("MAPBOX_TOKEN")
    response = requests.get(f"https://api.mapbox.com/directions/v5/mapbox/cycling/{startLong},{startLat};{endLong},{endLat}?geometries=geojson&access_token={token}")
    return HttpResponse(response)

# create a new route and redirect to maps
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

# delete a route
def deleteRoute(request):
    if request.method == "POST":
        routeName = request.POST.get("route_name")
        if Route.objects.filter(routeName=routeName).exists():
            Route.objects.filter(routeName=routeName).delete()
    return redirect("maps")