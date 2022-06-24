from django.db import models
from django.db.models.fields import CharField, IntegerField, EmailField

# Create your models here.
class ClientUser(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length= 50, default="operational")
    status = models.BooleanField(default=False, db_index=True)
    verified = models.BooleanField(default=False, db_index=True)
    def __str__(self) -> str:
        return self.email
