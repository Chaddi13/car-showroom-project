from django.db import models
from src.core.models.abstract_models import CreatedAt
from django.core.validators import MinValueValidator, MaxValueValidator


class SalesShowroomToCustomer(CreatedAt):
    showroom = models.ForeignKey(
        "showroom.Showroom",
        on_delete=models.PROTECT,
        related_name="showroom",
        null=True,
    )
    customer = models.ForeignKey(
        "customer.Customer",
        on_delete=models.PROTECT,
        related_name="customer_transaction_history",
        null=True,
    )
    car = models.ForeignKey(
        "car.Car", on_delete=models.PROTECT, related_name="sold_car", null=True
    )
    price = models.DecimalField(max_digits=15, decimal_places=2)
    amount_of_discount = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(30)]
    )

    class Meta:
        db_table = "sales_showroom_to_customer"

    def __str__(self):
        return f"{self.showroom} {self.customer} {self.car} {self.price} {self.amount_of_discount} {self.created_at}"


class SalesShipperToShowroom(CreatedAt):
    showroom = models.ForeignKey(
        "showroom.Showroom",
        on_delete=models.PROTECT,
        related_name="showroom_that_buys",
        null=True,
    )
    shipper = models.ForeignKey(
        "shipper.Shipper",
        on_delete=models.PROTECT,
        related_name="shipper_that_sells",
        null=True,
    )
    car = models.ForeignKey(
        "car.Car", on_delete=models.PROTECT, related_name="car_for_sale", null=True
    )
    price = models.DecimalField(max_digits=20, decimal_places=2)
    amount_of_discount = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(30)]
    )

    class Meta:
        db_table = "sales_dealer_to_showroom"

    def __str__(self):
        return f"{self.showroom} {self.shipper} {self.car} {self.price} {self.amount_of_discount} {self.created_at}"
