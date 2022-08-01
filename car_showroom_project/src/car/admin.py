from django.contrib import admin
from src.car.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    list_filter = (
        "make",
        "model",
        "body_type",
        "color",
        "horsepower",
        "year",
    )
