from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.maps, name="maps"),
    path("key",views.mapsKey, name="mapsKey"),
    path("directions/<str:modeOfTransport>/<str:startLong>,<str:startLat>;<str:endLong>,<str:endLat>", views.getDirections, name="getDirections"),
    path("newRoute/", views.createRoute, name="newRoute"),
    path("deleteRoute/", views.deleteRoute, name="deleteRoute")
]