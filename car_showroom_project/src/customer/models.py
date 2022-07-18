from django.db import models
from src.core.models.abstract_models import Info, CreatedAt, UpdatedAt
from django.core.validators import MinValueValidator, MaxValueValidator
from src.core.enums.enums import CustomerSex


class Customer(Info, CreatedAt, UpdatedAt):
    surname = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MinValueValidator(16), MaxValueValidator(120)])
    sex = models.CharField(max_length=20, choices=CustomerSex.choices())
    licence = models.BooleanField(default=True)

    class Meta:
        db_table = "customer"

    def __str__(self):
        return f"{self.name} {self.surname} {self.age} {self.sex} {self.email} {self.country}"


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
