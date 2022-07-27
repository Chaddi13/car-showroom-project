from rest_framework import routers

from src.transaction.views import (
    TransactionShipperToShowroomPublicView,
    TransactionShipperToShowroomPrivateView,
    TransactionShowroomToCustomerPublicView,
    TransactionShowroomToCustomerPrivateView
)

router = routers.DefaultRouter()
router.register(r"showroom/list", TransactionShowroomToCustomerPublicView, "Public Showroom Transaction")
router.register(r"showroom/private", TransactionShowroomToCustomerPrivateView, "Private Showroom Transaction")
router.register(r"shipper/list", TransactionShipperToShowroomPublicView, "Public Shipper Transaction")
router.register(r"shipper/private", TransactionShipperToShowroomPrivateView, "Private Shipper Transaction")

urlpatterns = router.urls