from django.core.management.base import BaseCommand
from faker import Faker
from commute.models import Driver, Car
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        num_drivers = 10
        self.populate_drivers(num_drivers)
        self.stdout.write(self.style.SUCCESS(f'{num_drivers} driver details created.'))

    def populate_drivers(self, num_drivers):
        for _ in range(num_drivers):
            car = Car.objects.create(
                make=fake.company(),
                model=fake.word(),
                color=fake.color_name(),
                plate_number=fake.license_plate(),
                number_of_seats=random.randint(2, 6)
            )
            driver = Driver.objects.create(
                user=None,  # Since there are no users in this scenario
                car=car
            )
