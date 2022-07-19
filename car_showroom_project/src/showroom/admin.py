from django.contrib import admin
from .models import Showroom, DiscountShowroom


@admin.register(Showroom)
class ShowroomAdmin(admin.ModelAdmin):
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    list_filter = (
        "name",
        "country",
        "is_active",
    )


@admin.register(DiscountShowroom)
class DiscountShowroomsAdmin(admin.ModelAdmin):
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    list_filter = (
        "start_time",
        "end_time",
        "amount_of_discount",
        "is_active",
        "created_at",
        "updated_at",
    )