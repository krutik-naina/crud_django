from django.db import models

# Create your models here.

class Examples (models.Model):
    oname = models.CharField(max_length=30)
    oemail = models.CharField(max_length=30)
    ophone = models.IntegerField()
    ocity = models.CharField(max_length=30)