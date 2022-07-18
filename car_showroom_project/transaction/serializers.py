from customer_app.serializers import CustomerShortInfoSerializer
from car_app.serializers import CarSerializer
from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers
from showroom_app.serializers import ShortShowroomSerializer

from .models import SalesShipperToShowroom, SalesShowroomToCustomer


class SalesShowroomToBuyersSerializer(CountryFieldMixin, serializers.ModelSerializer):
    showroom = ShortShowroomSerializer(read_only=True)
    customer = CustomerShortInfoSerializer(read_only=True)
    car = CarSerializer(read_only=True)

    class Meta:
        model = SalesShowroomToCustomer
        fields = ["showroom", "customer", "car", "price", "amount_of_discount"]


class SalesShipperToShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesShipperToShowroom
        fields = "__all__"
