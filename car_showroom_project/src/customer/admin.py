from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Customer, CustomerOrder


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_filter =(
        "id",
        "username",
        "balance",
        "is_active",
    )

    list_display = (
        "id",
        "username",
        "balance",
        "is_active",
    )

    list_editable = (
        "is_active",
    )

    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            "Custom fields",
            {
                "fields": (
                    "car_characteristics",
                    "age",
                    "sex",
                    "balance",
                    "country",
                )
            }
        )
    )

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            "Custom fields",
            {
                "fields": (
                    "car_characteristics",
                    "age",
                    "sex",
                    "balance",
                    "country",
                )
            }
        )
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
