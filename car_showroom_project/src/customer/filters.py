from django_filters import rest_framework as filters
from .models import CustomerOrder


class CustomerFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="id_buyer__name", lookup_expr="exact")
    surname = filters.CharFilter(field_name="id_buyer__surname", lookup_expr="exact")
    age = filters.NumberFilter(field_name="id_buyer__age", lookup_expr="exact")
    sex = filters.CharFilter(field_name="id_buyer__sex", lookup_expr="exact")
    email = filters.CharFilter(field_name="id_buyer__email", lookup_expr="exact")
    created_at = filters.DateFilter(
        field_name="id_buyer__created_at", lookup_expr="exact"
    )
    updated_at = filters.DateFilter(
        field_name="id_buyer__updated_at", lookup_expr="exact"
    )
    id_buyer = filters.NumberFilter(field_name="id_buyer", lookup_expr="exact")
    id_car = filters.NumberFilter(field_name="id_car", lookup_expr="exact")
    price = filters.NumberFilter(field_name="price", lookup_expr="exact")
    is_available = filters.BooleanFilter(field_name="is_available", lookup_expr="exact")
    order_created_at = filters.DateFilter(field_name="order_created_at", lookup_expr="exact")
    order_updated_at = filters.DateFilter(
        field_name="order_updated_at", lookup_expr="exact"
    )

    class Meta:
        model = CustomerOrder
        fields = ()
