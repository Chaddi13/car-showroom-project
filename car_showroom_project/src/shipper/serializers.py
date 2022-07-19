from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers
from .models import Shipper, DiscountShipper
from src.car.serializers import CarSerializer


class ShipperSerializer(CountryFieldMixin, serializers.ModelSerializer):
    shippers_cars = CarSerializer(many=True, read_only=True)
    total_cars = serializers.SerializerMethodField()

    class Meta:
        model = Shipper
        fields = [
            "name",
            "email",
            "found_year",
            "description",
            "total_cars",
            "shippers_cars",
        ]

    def get_total_cars(self, instance):
        return instance.shippers_cars.count()


class DiscountShipperSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountShipper
        fields = "__all__"
