from django.db import models

# Create your models here.

class Population(models.Model):
    census_tract = models.FloatField(default=0.0)
    pop_100 = models.IntegerField(default=0)
