from django.db import models
from src.core.models.abstract_models import BusinessInfo, Info, IsActive, CreatedAt, UpdatedAt, Discount


class Showroom(BusinessInfo, Info, IsActive, CreatedAt, UpdatedAt):
    class Meta:
        db_table = "showroom"

    def __str__(self):
        return f"{self.name} {self.description}"


class DiscountShowroom(CreatedAt, UpdatedAt, IsActive, Discount):
    showrooms_discount = models.ForeignKey(
        Showroom,
        on_delete=models.PROTECT,
        related_name="showroom_with_discount",
        null=True,
        verbose_name="showroom",
    )
    discount_showroom_for_car = models.ForeignKey(
        "car.Car",
        on_delete=models.PROTECT,
        related_name="showroom_car_on_sale",
        null=True,
        verbose_name="car",
    )

    class Meta:
        db_table = "showroom_discount"

    def __str__(self):
        return f"{self.start_time} {self.end_time} {self.amount_of_discount}"
