from django.db import models

# Create your models here.
class Myfile(models.Model):
    id=models.CharField(max_length=250,primary_key=True)
    file=models.FileField(upload_to="myfile")
date=models.DateField(auto_now_add=True)