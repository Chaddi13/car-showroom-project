from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers
from django.db.models import F

from src.shipper.models import Shipper
from src.car.serializers import CarSerializer
from src.showroom.serializers import ShowroomShortInfoSerializer


class ShipperSerializer(CountryFieldMixin, serializers.ModelSerializer):
    shippers_cars = CarSerializer(many=True, read_only=True)
    total_cars = serializers.SerializerMethodField()
    buyers = serializers.SerializerMethodField()

    class Meta:
        model = Shipper
        fields = [
            "name",
            "email",
            "country",
            "found_year",
            "description",
            "total_cars",
            "shippers_cars",
            "buyers",
        ]

    def get_total_cars(self, instance):
        return instance.shippers_cars.count()

    def get_buyers(self, instance):
        queryset = Shipper.objects.get(pk=instance.id)
        buyers = (
            queryset.shipper_that_sells.all()
            .values(name=F("showroom__name"), email=F("showroom__email"))
            .distinct()
            .order_by()
        )
        serializer_data = ShowroomShortInfoSerializer(buyers, many=True).data

        return serializer_data

class ShipperShortInfoSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Shipper
        fields = ["name", "email"]