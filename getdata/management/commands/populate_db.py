from django.core.management.base import BaseCommand
from getdata.models import Population

import pandas as pd


class Command(BaseCommand):
    # python manage.py populate_db

    def _put_population(self):

        # delete everything in the table
        Population.objects.all().delete()
        print("Reading Population data...")
        url = "http://censusdata.ire.org/17/all_140_in_17.P1.csv"
        c = pd.read_csv(url, usecols=[8,9])
        for entry in c.iterrows():
            # cleaning census tract number column
            census_tract = float(''.join(filter(lambda x: x.isdigit() or x == '.', entry[1]['NAME'])))
            # pull corresponding pop100
            pop_100 = entry[1]['POP100']
            # create Django object
            tract = Population(census_tract=census_tract, pop_100=pop_100)
            tract.save()
        print("Done")


    def handle(self, *args, **options):
        self._put_population()