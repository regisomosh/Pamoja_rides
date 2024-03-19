from django.contrib import admin
from .models import Driver, Car, Commute, Commuter

admin.site.register(Driver)
admin.site.register(Car)
admin.site.register(Commute)
admin.site.register(Commuter)