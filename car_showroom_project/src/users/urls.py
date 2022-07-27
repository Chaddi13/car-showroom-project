from rest_framework import routers

from src.users.views import UserPublicView

router = routers.SimpleRouter()
router.register(r"list", UserPublicView)

urlpatterns = router.urls
