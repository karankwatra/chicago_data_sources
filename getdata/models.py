from django.db import models

# Create your models here.

class Population(models.Model):
    census_tract = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    pop_100 = models.IntegerField(default=0)
