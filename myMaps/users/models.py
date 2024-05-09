from django.db import models
# from encrypted_model_fields.fields import EncryptedCharField


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    
class Path(models.Model):
    user_id = models.CharField(max_length=20)
    startPoint = models.JSONField()
    endPoint = models.JSONField()
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'startPoint': self.startPoint,
            'endPoint': self.endPoint,
        }
