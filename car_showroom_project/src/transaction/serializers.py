from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

from src.showroom.serializers import ShowroomShortInfoSerializer
from src.transaction.models import SalesShipperToShowroom, SalesShowroomToCustomer
from src.shipper.serializers import ShipperShortInfoSerializer
from src.customer.serializers import CustomerShortInfoSerializer
from src.car.serializers import CarSerializer


class SalesShowroomToBuyersSerializer(CountryFieldMixin, serializers.ModelSerializer):
    showroom = ShowroomShortInfoSerializer(read_only=True)
    customer = CustomerShortInfoSerializer(read_only=True)
    car = CarSerializer(read_only=True)

    class Meta:
        model = SalesShowroomToCustomer
        fields = ["showroom", "customer", "car", "price", "amount_of_discount"]


class SalesShipperToShowroomSerializer(serializers.ModelSerializer):
    shipper = ShipperShortInfoSerializer(read_only=True)
    showroom = ShowroomShortInfoSerializer(read_only=True)
    car = CarSerializer(read_only=True)

    class Meta:
        model = SalesShipperToShowroom
        fields = ["shipper", "showroom", "car", "price", "amount_of_discount"]
