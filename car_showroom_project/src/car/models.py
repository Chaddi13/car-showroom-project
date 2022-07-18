from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from src.core.models.abstract_models import CreatedAt, UpdatedAt
from src.core.enums.enums import CarColor, CarBodyType


class Car(CreatedAt, UpdatedAt):
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    body_type = models.CharField(max_length=40, choices=CarBodyType.choices())
    color = models.CharField(max_length=20, choices=CarColor.choices())
    horsepower = models.PositiveIntegerField()
    year = models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2025)])
    price = models.DecimalField(max_digits=15, decimal_places=2)
    showroom = models.ForeignKey(
        "showroom.Showroom",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="showrooms_cars",
    )
    shipper = models.ForeignKey(
        "shipper.Shipper",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="shippers_cars",
    )
    customer = models.ForeignKey(
        "customer.Customer",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="customers_cars",
    )

    class Meta:
        db_table = "car"

    def __str__(self):
        return f"{self.make} {self.model}"
