import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myMaps.settings")
django.setup()

from users.models import User, Path

def query_records():
    records = User.objects.all()
    for record in records:
        print(record.username)

def delete_all_records():
    # Delete all records from the model
    User.objects.all().delete()
# delete_all_records()

def create_path():
    newPath = Path(user_id="pavlos1",startPoint={"lat":34.658383, "long": 32.961000}, endPoint={"lat":34.874886, "long": 32.736756})
    newPath.save()

def query_records_paths():
    records = Path.objects.all()
    for record in records:
        print(record.user_id, record.startPoint, record.endPoint)

# create_path()
# query_records_paths()
