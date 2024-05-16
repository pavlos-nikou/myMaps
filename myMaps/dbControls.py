import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myMaps.settings")
django.setup()

from users.models import User, Route

def query_records():
    records = User.objects.all()
    for record in records:
        print(record.username)

def delete_all_records():
    # Delete all records from the model
    User.objects.all().delete()
# delete_all_records()

def create_path():
    newPath = Route(user_id="pavlos1", routeName="Route3", startPoint={"lat":34.686647, "long": 32.005162}, endPoint={"lat":34.875084, "long": 32.736881})
    newPath.save()

def query_records_paths():
    records = Route.objects.all()
    for record in records:
        print(record.user_id, record.routeName, record.startPoint, record.endPoint)

def delete_all_records_paths():
    Route.objects.all().delete()

create_path()
# delete_all_records_paths()
query_records_paths()
