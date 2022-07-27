from rest_framework import routers

from src.shipper.views import ShipperPublicView, ShipperPrivateView

router = routers.DefaultRouter()
router.register(r"list", ShipperPublicView, "Public Shipper")
router.register(r"private", ShipperPrivateView, "Private Shipper")

urlpatterns = router.urls
