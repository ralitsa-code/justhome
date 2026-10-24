from django.core.validators import RegexValidator
from django.db import models


class Broker(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message="Phone number must contain 10 digits without spaces."
            )
        ]
    )

    picture = models.ImageField(
        blank=True,
        null=True,
        upload_to='broker/',
    )