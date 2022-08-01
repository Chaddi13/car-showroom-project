from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated

from src.showroom.filters import ShowroomFilter
from src.showroom.models import Showroom
from src.showroom.serializers import MainShowroomSerializer


class ShowroomPublicView(ReadOnlyModelViewSet):
    """View information about Showrooms"""

    queryset = Showroom.objects.all()
    serializer_class = MainShowroomSerializer
    permission_classes = (AllowAny,)
    filterset_class = ShowroomFilter
    # filter_backends = (SearchFilter, OrderingFilter)
    # search_fields = ("name",)

class ShowroomPrivateView(ModelViewSet):
    """View and edit information about Showrooms"""

    queryset = Showroom.objects.all()
    serializer_class = MainShowroomSerializer
    permission_classes = (IsAuthenticated,)
    filterset_class = ShowroomFilter
    # filter_backends = (SearchFilter, OrderingFilter)
    # search_fields = ("name",)