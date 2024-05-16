from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    
class Route(models.Model):
    user_id = models.CharField(max_length=20)
    routeName = models.CharField(max_length=100)
    startPoint = models.JSONField()
    endPoint = models.JSONField()
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'routeName': self.routeName,
            'startPoint': self.startPoint,
            'endPoint': self.endPoint
        }
