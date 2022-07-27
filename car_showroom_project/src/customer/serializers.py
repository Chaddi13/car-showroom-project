from src.car.serializers import CarSerializer
from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

from .models import Customer, CustomerOrder


class CustomerOrderSerializer(serializers.ModelSerializer):
    car = CarSerializer(read_only=True)

    class Meta:
        model = CustomerOrder
        fields = ["price", "car"]


class CustomerSerializer(CountryFieldMixin, serializers.ModelSerializer):
    customer_orders = CustomerOrderSerializer(read_only=True, many=True)

    class Meta:
        model = Customer
        fields = [
            "name",
            "surname",
            "email",
            "balance",
            "country",
            "age",
            "sex",
            "licence",
            "customer_orders",
        ]


class CustomerShortInfoSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["name", "surname"]
