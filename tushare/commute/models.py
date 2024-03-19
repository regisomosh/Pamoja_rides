from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    plate_number = models.CharField(max_length=20)
    number_of_seats = models.IntegerField()

    def __str__(self):
        return f"{self.plate_number}"

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user}"

class Commuter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user}"

class Commute(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    commuter = models.ForeignKey(Commuter, on_delete=models.CASCADE)
    departure_location = models.CharField(max_length=255)
    destination_location = models.CharField(max_length=255)
    available_seats = models.IntegerField()
    fare = models.DecimalField(max_digits=10, decimal_places=2)
    departure_time = models.DateTimeField()
    estimated_arrival_time = models.DateTimeField()
    def __str__(self):
        return f"Commute #{self.id}"
