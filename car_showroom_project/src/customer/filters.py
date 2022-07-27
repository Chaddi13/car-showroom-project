from django_filters import rest_framework as filters
from .models import Customer


class CustomerFilter(filters.FilterSet):
    class Meta:
        model = Customer
        fields = {
            "name":["iexact"],
            "surname":["iexact"],
            "country": ["icontains"],
            "age":["exact", "lt", "gt"]
        }
