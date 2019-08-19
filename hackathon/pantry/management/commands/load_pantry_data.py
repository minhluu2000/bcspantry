from csv import DictReader

from django.core.management import BaseCommand

from pantry.models import Pantry

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the pantry data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""

class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from Pantry_data.csv into our Pantry model"

    def handle(self, *args, **options):
        if Pantry.objects.exists() or Pantry.objects.exists():
            print('Pantry data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Loading Pantry data for pantries available for listing")
        for row in DictReader(open('./pantry_data.csv')):
            pantry = Pantry()
            pantry.name = row['name']
            pantry.address = row['address']
            pantry.mon = row['mon']
            pantry.tue = row['tue']
            pantry.wed = row['wed']
            pantry.thur = row['thur']
            pantry.fri = row['fri']
            pantry.sat = row['sat']
            pantry.sun = row['sun']
            pantry.website = row['website']
            pantry.map_link = row['map_link']
            pantry.save()
