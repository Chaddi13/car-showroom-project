from django_filters import rest_framework as filters
from django_filters.rest_framework import FilterSet

from src.transaction.models import SalesShipperToShowroom, SalesShowroomToCustomer


class ShowroomToCustomerFilter(FilterSet):
    model = SalesShowroomToCustomer
    fields = {
        "car__make": ["iexact"],
        "car__model": ["iexact"],
        "customer__name": ["iexact"],
        "showroom__name": ["iexact"],
        "price": ["exact", "lt", "gt"],
        "created_at": ["exact", "lt", "gt"],
    }


class ShipperToShowroomFilter(FilterSet):
    model = SalesShipperToShowroom
    fields = {
        "car__make": ["iexact"],
        "car__model": ["iexact"],
        "shipper__name": ["iexact"],
        "showroom__name": ["iexact"],
        "price": ["exact", "lt", "gt"],
        "created_at": ["exact", "lt", "gt"],
    }
