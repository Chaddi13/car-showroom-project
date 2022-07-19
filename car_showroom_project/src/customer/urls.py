from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from src.customer.views import CustomerListAPIView, get_details

urlpatterns = [
    path("customer/", CustomerListAPIView.as_view()),
    path("customer/details/<int:pk>", get_details),
]

urlpatterns = format_suffix_patterns(urlpatterns)
