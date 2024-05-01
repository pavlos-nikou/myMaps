from django.shortcuts import render, HttpResponse
from dotenv import load_dotenv
import os 

# Create your views here.
def maps(request):
    return render(request, "maps.html")

def mapsKey(request):
    load_dotenv()
    return HttpResponse(os.environ.get("MAPBOX_TOKEN"))