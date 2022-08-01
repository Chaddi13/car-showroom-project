from django.contrib import admin
from src.transaction.models import SalesShipperToShowroom, SalesShowroomToCustomer


@admin.register(SalesShowroomToCustomer)
class SalesShowroomsBuyersAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at",)
    list_filter = ("price", "amount_of_discount", "created_at")


@admin.register(SalesShipperToShowroom)
class SalesSuppliersShowroomsAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at",)
    list_filter = ("price", "amount_of_discount", "created_at")
