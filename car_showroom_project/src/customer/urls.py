from rest_framework import routers

from src.customer.views import CustomerPublicView, CustomerPrivateView


router = routers.DefaultRouter()
router.register(r"list", CustomerPublicView, "PublicCustomer")
router.register(r"private", CustomerPrivateView, "Private Customer")

urlpatterns = router.urls
