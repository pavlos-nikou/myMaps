from django.shortcuts import render, HttpResponse
from dotenv import load_dotenv
import os
from users.models import Path
import json


# Create your views here.
def maps(request):
    print(request.session.get("username"))
    paths = Path.objects.filter(user_id=request.session.get("username"))
    paths_json = json.dumps([path.to_dict() for path in paths])
    return render(request, "maps.html",{"paths": paths_json})

def mapsKey(request):
    load_dotenv()
    return HttpResponse(os.environ.get("MAPBOX_TOKEN"))