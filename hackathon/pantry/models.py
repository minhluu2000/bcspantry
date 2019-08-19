from django.db import models

class Pantry(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    # --- Available time of each day ---
    mon = models.CharField(max_length=30)
    tue = models.CharField(max_length=30)
    wed = models.CharField(max_length=30)
    thur = models.CharField(max_length=30)
    fri = models.CharField(max_length=30)
    sat = models.CharField(max_length=30)
    sun = models.CharField(max_length=30)
    # --- Available time of each day ---
    website = models.TextField() # URL to the application for food pantry
    map_link = models.TextField() # URL to map picture of food pantry
