from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny

from src.transaction.filters import ShipperToShowroomFilter, ShowroomToCustomerFilter
from src.transaction.models import SalesShipperToShowroom, SalesShowroomToCustomer
from src.transaction.serializers import (
    SalesShipperToShowroomSerializer,
    SalesShowroomToBuyersSerializer,
)


class TransactionShowroomToCustomerPublicView(ReadOnlyModelViewSet):
    """View information about Shippers"""

    queryset = SalesShowroomToCustomer.objects.all()
    serializer_class = SalesShowroomToBuyersSerializer
    permission_classes = (AllowAny,)
    filterset_class = ShowroomToCustomerFilter


class TransactionShowroomToCustomerPrivateView(ModelViewSet):
    """View information about Shippers"""

    queryset = SalesShowroomToCustomer.objects.all()
    serializer_class = SalesShowroomToBuyersSerializer
    permission_classes = (IsAuthenticated,)
    filterset_class = ShowroomToCustomerFilter


class TransactionShipperToShowroomPublicView(ReadOnlyModelViewSet):
    """View information about Shippers"""

    queryset = SalesShipperToShowroom.objects.all()
    serializer_class = SalesShipperToShowroomSerializer
    permission_classes = (AllowAny,)
    filterset_class = ShipperToShowroomFilter


class TransactionShipperToShowroomPrivateView(ModelViewSet):
    """View information about Shippers"""

    queryset = SalesShipperToShowroom.objects.all()
    serializer_class = SalesShipperToShowroomSerializer
    permission_classes = (IsAuthenticated,)
    filterset_class = ShipperToShowroomFilter
