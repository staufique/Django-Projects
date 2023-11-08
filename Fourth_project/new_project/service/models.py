from django.db import models

# Create your models here.

class myServices(models.Model):
    s_icon=models.CharField(max_length=50)
    s_title=models.CharField(max_length=50)
    s_desc=models.TextField()
    