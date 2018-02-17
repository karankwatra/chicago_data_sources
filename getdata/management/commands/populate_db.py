from django.core.management.base import BaseCommand
from getdata.models import Population

import pandas as pd


class Command(BaseCommand):
    # python manage.py populate_db

    def _put_population(self):
        tract = Population(census_tract=1.1, pop_100=100)
        print("saving to db")
        url = "http://censusdata.ire.org/17/all_140_in_17.P1.csv"
        c = pd.read_csv(url)
        print(c)

        # TODO
        # read in the 2 cols u need using pandas ^
        # Install Django-rest framework
        # Create Serializer, Viewset, and Routers
        # Configure Vue.js  with Django
        # https://medium.com/quick-code/crud-app-using-vue-js-and-django-516edf4e4217

        tract.save()


    def handle(self, *args, **options):
        self._put_population()