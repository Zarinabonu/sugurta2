from django.db import models

from app.model.currency import Republic


class Client(models.Model):
    INDIVIDUAL = '0'
    LOYAL = '1'
    TYPES = (
        (INDIVIDUAL, 'ФИЗ'),
        (LOYAL, 'ЮРД'),
    )
    type = models.CharField(TYPES, null=True, blank=True, max_length=128)
    republic = models.ForeignKey(Republic, on_delete=models.SET_NULL, null=True)
    resident = models.BooleanField(default=False)
