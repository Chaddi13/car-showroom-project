from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated

from src.shipper.filters import ShipperFilter
from src.shipper.models import Shipper
from src.shipper.serializers import ShipperSerializer


class ShipperPublicView(ReadOnlyModelViewSet):
    """View information about Shippers"""

    queryset = Shipper.objects.all()
    serializer_class = ShipperSerializer
    permission_classes = (AllowAny,)
    filterset_class = ShipperFilter
    # filter_backends = (SearchFilter, OrderingFilter)
    # search_fields = ("name",)


class ShipperPrivateView(ModelViewSet):
    """View and edit information about Shippers"""

    queryset = Shipper.objects.all()
    serializer_class = ShipperSerializer
    permission_classes = (IsAuthenticated,)
    filterset_class = ShipperFilter
    # filter_backends = (SearchFilter, OrderingFilter)
    # search_fields = ("name",)
