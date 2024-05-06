from django.db import models
# from encrypted_model_fields.fields import EncryptedCharField


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    def _str_(self):
        return self.name
    
class Path(models.Model):
    startPoint = models.JSONField()
    endPoint = models.JSONField()
