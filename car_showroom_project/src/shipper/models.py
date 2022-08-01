from django.db import models
from src.core.models.abstract_models import IsActive, CreatedAt, UpdatedAt, BusinessInfo, Info
from .utils import DiscountRanks


class Shipper(BusinessInfo, Info, IsActive, CreatedAt, UpdatedAt):
    number_of_buyers = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "shipper"

    def __str__(self):
        return f"{self.name} {self.description}"


class DiscountShipper(models.Model):
    discount = models.IntegerField(
        choices=DiscountRanks.DISCOUNT_CHOICES, default=DiscountRanks.REGULAR
    )
    bought_cars = models.PositiveIntegerField(default=0)
    showroom = models.ForeignKey(
        "showroom.Showroom",
        related_name="showroom_discounts",
        on_delete=models.CASCADE,
        null=True,
    )
    shipper = models.ForeignKey(
        "shipper.Shipper",
        related_name="shipper_discounts",
        on_delete=models.CASCADE,
        null=True,
    )

    class Meta:
        db_table = "shipper_discount"
        unique_together = ["showroom", "shipper"]

    def __str__(self):
        return f"{self.discount} {self.bought_cars} {self.showroom} {self.shipper}"
