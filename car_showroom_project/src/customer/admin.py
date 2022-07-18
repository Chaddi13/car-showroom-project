from django.contrib import admin
from src.customer.models import Customer, CustomerOrder


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    list_filter = (
        "name",
        "surname",
        "age",
        "sex",
        "country",
        "created_at",
        "updated_at",
    )


@admin.register(CustomerOrder)
class CustomerOrderAdmin(admin.ModelAdmin):
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    list_filter = (
        "price",
        "created_at",
        "updated_at",
    )
