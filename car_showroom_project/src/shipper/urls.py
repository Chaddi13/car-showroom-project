from django.urls import include, path
from rest_framework import routers

from .views import ShipperViewSet

router = routers.DefaultRouter()
router.register(r"shipper", ShipperViewSet, basename="shipper")

urlpatterns = [path("", include(router.urls))]