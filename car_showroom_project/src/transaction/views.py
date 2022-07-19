from src.core.api_interface.api_interface import CustomViewSet
from src.core.permissions.permissions import IsCustomerUser, IsShipperUser, IsShowroomUser
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .filters import ShipperToShowroomFilter, ShowroomToCustomerFilter
from .models import SalesShipperToShowroom, SalesShowroomToCustomer
from .serializers import (
    SalesShipperToShowroomSerializer,
    SalesShowroomToBuyersSerializer,
)


class TransactionShowroomToCustomerViewSet(CustomViewSet):
    """View for transactions from Showroom to customer"""

    queryset = SalesShowroomToCustomer.objects.all()
    serializer_class = SalesShowroomToBuyersSerializer
    permission_classes = [(IsShowroomUser | IsCustomerUser | IsAdminUser)]
    filterset_class = ShowroomToCustomerFilter

    @action(methods=["get"], detail=False, url_path="history")
    def list_of_transactions(self, request):
        """Return transactions list from Showroom to customers"""
        return super(TransactionShowroomToCustomerViewSet, self).get(request)

    @action(methods=["get"], detail=True, url_path="showroom-details")
    def showroom_to_customer_transaction_history(self, request, pk):
        showroom_transaction = SalesShowroomToCustomer.objects.filter(showroom=pk)
        serializer_data = SalesShowroomToBuyersSerializer(
            showroom_transaction, many=True
        ).data
        return Response(
            {"Transaction history for showroom": serializer_data},
            status=status.HTTP_200_OK,
        )

    @action(methods=["get"], detail=True, url_path="customer-details")
    def details_of_transaction(self, request, pk):
        """Return list of customer transactions"""
        customers_transactions = SalesShowroomToCustomer.objects.filter(customer=pk)
        data = SalesShowroomToBuyersSerializer(customers_transactions, many=True).data
        return Response(
            {"Transaction history for customer": data}, status=status.HTTP_200_OK
        )


class TransactionShipperToShowroomViewSet(CustomViewSet):
    queryset = SalesShipperToShowroom.objects.all()
    serializer_class = SalesShipperToShowroomSerializer
    permission_classes = [(IsShipperUser | IsShowroomUser | IsAdminUser)]
    filterset_class = ShipperToShowroomFilter

    @action(methods=["get"], detail=False, url_path="history")
    def list_of_transactions(self, request):
        """Return transactions list from Dealer to Showroom"""
        return super(TransactionShipperToShowroomViewSet, self).get(request)

    @action(methods=["get"], detail=True, url_path="details")
    def details_of_transaction(self, request, pk):
        """Return list of customer transactions"""
        shipper_transactions = SalesShipperToShowroom.objects.filter(shipper=pk)
        data = SalesShipperToShowroomSerializer(shipper_transactions, many=True).data
        return Response(
            {"Transaction history to shipper": data}, status=status.HTTP_200_OK
        )


class DiscountViewSet(CustomViewSet):
    """
    A viewset for discounts of showrooms and suppliers
    """

    pass
