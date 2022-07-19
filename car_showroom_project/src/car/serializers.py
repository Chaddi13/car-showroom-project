from rest_framework import serializers

from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ["make", "model", "body_type", "color", "horsepower", "year"]
