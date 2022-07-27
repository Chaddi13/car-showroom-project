from django.db.models import Count, F
from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

from src.showroom.models import Showroom
from src.car.serializers import CarSerializer
from src.customer.serializers import CustomerShortInfoSerializer


class MainShowroomSerializer(CountryFieldMixin, serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)
    total_cars = serializers.SerializerMethodField()
    buyers = serializers.SerializerMethodField()

    class Meta:
        model = Showroom
        fields = ["name", "country", "found_year", "email", "balance", "description", "cars", "total_cars", "buyers"]

    def get_total_cars(self, instance):
        return instance.showrooms_cars.all().count()

    def get_buyers(self, instance):
        queryset = Showroom.objects.get(pk=instance.id)
        buyers = (
            queryset.showroom.all()
            .values(name=F("customer__name"), surname=F("customer__surname"))
            .distinct()
            .order_by()
        )
        serializer_data = CustomerShortInfoSerializer(buyers, many=True).data

        return serializer_data


class ShowroomShortInfoSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Showroom
        fields = ["name", "email"]
