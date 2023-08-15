from django.db import models


class Car(models.Model):

    class ManufacturerChoices(models.TextChoices):
        TOYOTA = 'Toyota'
        HONDA = 'Honda'
        FORD = 'Ford'
        BMW = 'BMW'
        OTHER = 'Other'
    
    manufacturer = models.CharField(
        max_length=20,
        choices=ManufacturerChoices.choices,
        default=ManufacturerChoices.OTHER,
    )
    model_name = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=20)
    engine_capacity = models.DecimalField(max_digits=4, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    transmission = models.CharField(max_length=20, null=True)
    mileage = models.PositiveIntegerField(default=0)
    num_seats = models.PositiveIntegerField(default=0)
    is_hybrid = models.BooleanField(default=False)
    is_electric = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.year} {self.manufacturer} {self.model_name}"
