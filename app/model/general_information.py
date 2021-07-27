from django.db import models

from app.model.currency import Currency, Republic
from app.model.employee import Employee


class Insurance_class(models.Model):
    name = models.TextField(default='', null=True, blank=True)


class General_information(models.Model):
    insurance_class = models.ForeignKey(Insurance_class, on_delete=models.SET_NULL, null=True)
    date_conclusion = models.DateField()
    start_period = models.DateField()
    finish_period = models.DateField()
    days = models.IntegerField(default='', null=True, blank=True)
    insurer = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    currency_condition = models.TextField(null=True, blank=True)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True)
    geographic_area = models.ForeignKey(Republic, on_delete=models.SET_NULL, null=True)
    contract_number = models.TextField()
    insured_person = models.ForeignKey()
    vigod_acquirer = models.ForeignKey()

