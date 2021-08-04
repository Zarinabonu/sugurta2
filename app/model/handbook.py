from django.db import models


class Currency(models.Model):
    name = models.TextField(null=True, blank=True)


class City(models.Model):
    name = models.TextField(null=True, blank=True)


class Region(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.TextField(null=True, blank=True)


class District(models.Model):
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.TextField(null=True, blank=True)


class Okonx(models.Model):
    name = models.TextField(null=True, blank=True)


class Polis(models.Model):
    name = models.TextField(null=True, blank=True)


