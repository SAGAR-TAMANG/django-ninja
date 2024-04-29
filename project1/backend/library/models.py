from django.db import models

# Create your models here.
class Library(models.Model):
  id = models.IntegerField(max_length=155, primary_key=True)
  name = models.CharField(max_length=155)

  