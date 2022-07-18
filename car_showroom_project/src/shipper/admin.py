from django.contrib import admin
from src.shipper.models import Shipper


@admin.register(Shipper)
class ShipperAdmin(admin.ModelAdmin):
    readonly_fields = (
        "created_at",
        "updated_at",
        "number_of_buyers",
    )
    list_filter = (
        "name",
        "country",
        "number_of_buyers",
        "is_active",
        "created_at",
        "updated_at",
    )
