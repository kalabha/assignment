from django.db import models
from geoposition.fields import GeopositionField


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.name)


class State(models.Model):
    name = models.CharField(max_length=100, unique=True)

    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=True, related_name="states")

    def __str__(self):
        return str(self.name)


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    state = models.ForeignKey(State, on_delete=models.CASCADE, default=True, related_name="cities")

    def __str__(self):
        return str(self.name)


class Address(models.Model):
    addressline1 = models.CharField("Addressline 1", max_length=200)
    addressline2 = models.CharField("Addressline 2", max_length=200)
    area = models.CharField(max_length=100)
    zipcode = models.IntegerField(null=True, blank=True)

    country = models.ForeignKey('Country', on_delete=models.CASCADE)

    state = models.ForeignKey('State', on_delete=models.CASCADE)

    city = models.ForeignKey('City', on_delete=models.CASCADE)


class Contact(models.Model):
    phone = models.CharField("Phone Number", max_length=20)
    alternate_phone = models.CharField("Alternate Phone Number", max_length=20, null=True, blank=True)


class Coordinate(models.Model):
    values = GeopositionField()
    address = models.TextField()

    def __str__(self):
        return str(self.values)