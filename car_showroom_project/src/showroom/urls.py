from rest_framework import routers

from .views import ShowroomPublicView, ShowroomPrivateView

router = routers.DefaultRouter()
router.register(r"list", ShowroomPublicView, "Public Showroom")
router.register(r"private", ShowroomPrivateView, "Private Showroom")

urlpatterns = router.urls
