from django_filters import rest_framework as filters

from .models import Shipper


class ShipperFilter(filters.FilterSet):
    class Meta:
        model = Shipper
        fields = {
            "name": ["icontains"],
            "country": ["icontains"],
            "number_of_buyers":["exact", "lt", "gt"],
        }