from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

from src.core.models.abstract_models import Info, CreatedAt, UpdatedAt
from src.core.enums.enums import CustomerSex


def default_characteristics():
    return {"make": "BMW",
            "model": "X5",
            "body_type": "Универсал",
            "color": "Черный",
            "year": 2021,
            "horsepower": 900, }


class Customer(Info, CreatedAt, UpdatedAt, AbstractUser):
    age = models.IntegerField(validators=[MinValueValidator(16), MaxValueValidator(120)], null=True)
    sex = models.CharField(max_length=255, choices=CustomerSex.choices())
    licence = models.BooleanField(default=True)
    car_characteristics = models.JSONField(
        encoder=None,
        decoder=None,
        default=default_characteristics
    )

    class Meta:
        db_table = "customer"

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.age} {self.sex} {self.email} {self.country}"


class CustomerOrder(CreatedAt, UpdatedAt):
    customer = models.ForeignKey(
        Customer, on_delete=models.PROTECT, related_name="customer_orders", null=True
    )
    car = models.ForeignKey(
        "car.Car", on_delete=models.PROTECT, related_name="ordered_car", null=True
    )
    price = models.DecimalField(max_digits=25, decimal_places=2)

    class Meta:
        db_table = "customer_order"

    def __str__(self):
        return f"{self.customer} {self.car} {self.price}"
