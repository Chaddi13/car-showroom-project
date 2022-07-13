from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from core.models.abstract_models import CreatedAt, UpdatedAt


class Car(CreatedAt, UpdatedAt):
    CHOICES = [
        ("SEDAN", "Седан"),
        ("COUPE", "Купе"),
        ("SPORT", "Спорткар"),
        ("WAGON", "Универсал"),
        ("HATCHBACK", "Хэтчбэк"),
        ("CONVERTIBLE", "Кабриолет"),
        ("MINIVAN", "Минивэн"),
    ]
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    body_type = models.CharField(max_length=40, choices=CHOICES)
    color = models.CharField(max_length=20)
    horsepower = models.IntegerField()
    year = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2025)])
    price = models.DecimalField(max_digits=15, decimal_places=2)
    showroom = models.ForeignKey(
        "showroom_app.Showroom",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="showrooms_cars",
    )
    shipper = models.ForeignKey(
        "shipper_app.Shipper",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="shippers_cars",
    )
    customer = models.ForeignKey(
        "customer_app.Customer",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="customers_cars",
    )

    class Meta:
        db_table = "car"

    def __str__(self):
        return f"{self.make} {self.model}"
