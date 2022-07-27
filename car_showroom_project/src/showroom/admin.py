from django.contrib import admin
from .models import Showroom, DiscountShowroom


@admin.register(Showroom)
class ShowroomAdmin(admin.ModelAdmin):
    readonly_fields = (
        "created_at",
        "updated_at",
        "unique_buyers",
        "total_cars",
    )
    list_filter = (
        "name",
        "country",
        "is_active",
    )

    def unique_buyers(self, instance):
        names = Showroom.objects.get(pk=instance.id).showroom.values("customer__name").distinct()
        buyers = []
        for x in range(len(names)):
            buyers.append(names[x]["customer__name"])
        return ', '.join(buyers)

    def total_cars(self, instance):
        return Showroom.objects.get(pk=instance.id).showrooms_cars.values("make").count()


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