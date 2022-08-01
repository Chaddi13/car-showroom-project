from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated

from src.customer.filters import CustomerFilter
from src.customer.models import Customer
from src.customer.serializers import CustomerSerializer


class CustomerPublicView(ReadOnlyModelViewSet):
    """View information about Customers"""

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (AllowAny,)
    filterset_class = CustomerFilter
    # filter_backends = (SearchFilter, OrderingFilter)
    # search_fields = ("name",)


class CustomerPrivateView(ModelViewSet):
    """View and edit information about Customers"""

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (IsAuthenticated,)
    filterset_class = CustomerFilter
    # filter_backends = (SearchFilter, OrderingFilter)
    # search_fields = ("name",)
