from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from src.users.models import ShowroomUser
from src.users.serializers import ShowroomUserSerializer


# class ShowroomUserViewSet(CustomViewSet):
#     queryset = ShowroomUser.objects.all()
#     serializer_class = ShowroomUserSerializer
#     filter_backends = (SearchFilter, OrderingFilter)
#     search_fields = ("username",)
#
#     @action(
#         detail=False,
#         methods=["get"],
#         permission_classes=[AllowAny],
#         url_path="list",
#     )
#     def get(self, request):
#         return super(ShowroomUserViewSet, self).get(request)
#
#     @action(
#         ["get"],
#         detail=True,
#         permission_classes=[AllowAny],
#         url_path="details",
#     )
#     def get_details(self, request, pk):
#         showroom_user_detail = ShowroomUser.objects.get(pk=pk)
#         data = ShowroomUserSerializer(showroom_user_detail).data
#         return Response({"shipper details": data})
#
#     @action(
#         detail=False,
#         permission_classes=[AllowAny],
#         methods=["post"],
#         url_path="create",
#     )
#     def post(self, request):
#         return super(ShowroomUserViewSet, self).post(request)
#
#     @action(
#         detail=True,
#         methods=["get", "put"],
#         permission_classes=[AllowAny],
#         url_path="update",
#     )
#     def put(self, request, pk):
#         # showroom_user_detail = ShowroomUser.objects.filter(pk=pk)
#         # data = ShowroomUserSerializer(showroom_user_detail).data
#         # if data.is_valid():
#         #     return Response({"shipper details": data})
#         # return super(ShowroomUserViewSet, self).put(request, pk)
#
#         instance = self.queryset.get(pk=pk)
#         serializer = self.serializer_class(instance, data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
#     @action(
#         detail=True,
#         methods=["delete"],
#         permission_classes=[AllowAny],
#         url_path="delete",
#     )
#     def delete(self, request, pk):
#         return super(ShowroomUserViewSet, self).delete(request, pk)


class UserPublicView(ModelViewSet):
    """View information about Shippers"""

    queryset = ShowroomUser.objects.all()
    serializer_class = ShowroomUserSerializer
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("username",)
