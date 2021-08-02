from django.db import models

from app.model.handbook import City, Region, District, Okonx
from app.model.portfolio import Portfolio


class Client(models.Model):
    INDIVIDUAL = '1'
    LOYAL = '2'
    TYPES = (
        (INDIVIDUAL, 'ФИЗ'),
        (LOYAL, 'ЮРД'),
    )
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    type = models.CharField(choices=TYPES, null=True, blank=True, max_length=128)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    resident = models.BooleanField(default=False)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    street = models.TextField(null=True, blank=True)
    house = models.TextField(null=True, blank=True)
    apartment = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    site = models.TextField(null=True, blank=True)
    postcode = models.TextField(null=True, blank=True)
    phone = models.TextField(null=True, blank=True)
    phone2 = models.TextField(null=True, blank=True)
    fax = models.TextField(null=True, blank=True)
    inn = models.TextField(null=True, blank=True)
    bank = models.TextField(null=True, blank=True)
    checking_account = models.TextField()
    mfo = models.TextField(null=True, blank=True)


class Loyal(models.Model):
    name = models.TextField(null=True, blank=True)
    okonx = models.ForeignKey(Okonx, on_delete=models.SET_NULL, null=True)
    okpo = models.TextField(null=True, blank=True)
    soato = models.TextField(blank=True, null=True)
    director = models.TextField(null=True, blank=True)
    accountant = models.TextField(null=True, blank=True)
    purpose = models.TextField(null=True, blank=True)
    bank_boolean = models.BooleanField(default=False)


class Individual(models.Model):
    MAN = '1'
    WOMAN = '2'
    GENDER = (
        (MAN, 'мужчина'),
        (WOMAN, 'женщина'),
    )

    passport = models.TextField(null=True, blank=True)
    passport_given = models.DateField(null=True, blank=True)
    given_date = models.DateField(null=True, blank=True)
    inps = models.TextField(null=True, blank=True)
    first_name = models.TextField(null=True, blank=True)
    last_name = models.TextField(null=True, blank=True)
    fath_name = models.TextField(null=True, blank=True)
    gender = models.CharField(choices=GENDER, null=True, blank=True, max_length=128)
    date_birth = models.DateField(null=True, blank=True)
    from_date = models.DateField(null=True, blank=True)
    finish_date = models.DateField(null=True, blank=True)
    chp = models.BooleanField(default=False)
