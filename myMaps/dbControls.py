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
query_records()