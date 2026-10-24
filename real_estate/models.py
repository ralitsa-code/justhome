from django.db import models
from broker.models import Broker
from features.models import Feature

class RealEstate(models.Model):
    class RealEstateType(models.TextChoices):
        HOUSE = 'HOUSE', "House"
        APARTMENT = 'APARTMENT', "Apartment"
        STUDIO = 'STUDIO', "Studio"

    real_estate_type = models.CharField(
        max_length=20,
        choices=RealEstateType.choices,
    )

    address = models.CharField(max_length=200)
    area = models.IntegerField(verbose_name="Area")
    price = models.IntegerField(verbose_name="Price")
    description = models.TextField(verbose_name="Description")

    broker = models.ForeignKey(
        Broker,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    feature = models.ManyToManyField(
        Feature,
        blank=True,
    )
