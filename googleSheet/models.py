from django.db import models


# Create your models here.
class Datas(models.Model):
    order = models.IntegerField(blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    price_in_rubles = models.FloatField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.date
