from src.core.api_interface.api_interface import CustomViewSet
from src.core.permissions.permissions import IsShipperUser
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .filters import ShipperFilter
from .models import Shipper
from .serializers import ShipperSerializer


class ShipperViewSet(CustomViewSet):
    """
    A viewset for information about shippers and theirs cars
    """

    queryset = Shipper.objects.all()
    serializer_class = ShipperSerializer
    permission_classes = [(IsShipperUser | IsAdminUser)]
    filterset_class = ShipperFilter
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("name",)

    @action(
        methods=["get"],
        detail=False,
        url_path="list",
    )
    def list_of_shippers(self, request):
        return super(ShipperViewSet, self).get(request)

    @action(methods=["get"], detail=True, url_path="details")
    def detail_of_shipper(self, request, pk):
        shipper_detail = Shipper.objects.get(pk=pk)
        data = ShipperSerializer(shipper_detail).data
        return Response({"shipper details": data}, status=status.HTTP_200_OK)

    @action(methods=["post"], url_path="create", detail=False)
    def create_shipper(self, request):
        return super(ShipperViewSet, self).post(request)

    @action(detail=True, methods=["delete"], url_path="delete")
    def delete(self, request, pk):
        return super(ShipperViewSet, self).delete(request, pk)
