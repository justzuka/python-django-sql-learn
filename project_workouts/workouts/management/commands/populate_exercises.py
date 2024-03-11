from django.core.management.base import BaseCommand
from ...exercise_data import populate_exercises

class Command(BaseCommand):
  help = "Populates the database with predefined exercises"

  def handle(self, *args, **options):
    populate_exercises()
    self.stdout.write(self.style.SUCCESS("Successfully populated exercises"))
