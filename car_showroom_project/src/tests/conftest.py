import pytest
from rest_framework.test import APIClient
from src.users.models import ShowroomUser


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def auth_client():
    auth_client = APIClient()
    user = ShowroomUser.objects.create_user(username='alex', password='alex123098')
    auth_client.force_login(user)
    return auth_client


# @pytest.fixture
# def model_list(auth_client):
#     response = client.get(url)
#     auth_response = auth_client.get(private_url)
#     non_auth_response = client.get(private_url)
#
#     responses = {
#         "response": response.status_code,
#         "auth_response": auth_response.status_code,
#         "non_auth_response": non_auth_response.status_code,
#     }
#
#     return responses
