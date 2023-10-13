from django.db import models


# Create your models here.
class Type(models.Model):
    type_id = models.CharField(max_length=50)
    type_name = models.CharField(max_length=50)


class Sport(models.Model):
    sport_id = models.CharField(max_length=50)
    sport_name = models.CharField(max_length=50)
    type = models.ManyToManyField(Type)


class Country(models.Model):
    country_id = models.CharField(max_length=50)
    country_name = models.CharField(max_length=50)


class Score(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    bronze = models.IntegerField(max_length=50)
    silver = models.IntegerField(max_length=50)
    gold = models.IntegerField(max_length=50)
