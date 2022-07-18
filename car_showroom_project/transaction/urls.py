from django.urls import include, path
from rest_framework import routers

from transaction.views import (
    TransactionShipperToShowroomViewSet,
    TransactionShowroomToCustomerViewSet,
)

router = routers.DefaultRouter()
router.register(r"transaction/showroom", TransactionShowroomToCustomerViewSet)
router.register(r"transaction/shipper", TransactionShipperToShowroomViewSet)

urlpatterns = [path("", include(router.urls))]