from django.contrib import admin

from src.shipper.models import Shipper, DiscountShipper


@admin.register(Shipper)
class ShipperAdmin(admin.ModelAdmin):
    readonly_fields = (
        "created_at",
        "updated_at",
        "number_of_buyers",
        "unique_buyers",
        "total_cars",
    )
    list_filter = (
        "name",
        "country",
        "number_of_buyers",
        "is_active",
        "created_at",
        "updated_at",
    )

    def unique_buyers(self, instance):
        names = Shipper.objects.get(pk=instance.id).shipper_that_sells.values("showroom__name").distinct()
        buyers = []
        for x in range(len(names)):
            buyers.append(names[x]["showroom__name"])
        return ', '.join(buyers)

    def total_cars(self, instance):
        return Shipper.objects.get(pk=instance.id).shippers_cars.values("make").count()


@admin.register(DiscountShipper)
class DiscountDealerAdmin(admin.ModelAdmin):
    list_filter = (
        "discount",
        "bought_cars",
        "showroom",
        "shipper",
    )
