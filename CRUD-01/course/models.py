from django.db import models

class User(models.Model):
    name=models.CharField(max_length=41)
    email=models.EmailField(max_length=25)
    password=models.CharField(max_length=12)