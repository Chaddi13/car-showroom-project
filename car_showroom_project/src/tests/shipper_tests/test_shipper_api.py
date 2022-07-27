import pytest
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from src.users.models import ShowroomUser
from src.shipper.models import Shipper


url = "/api/v1/shipper/list/"
private_url = "/api/v1/shipper/private/"

# class AccountTests(APITestCase):
#     user = ShowroomUser.objects.create_user(username='alex', password='wfii123098')
#
#
#     def test_get_shipper_list(self):
#         """
#         Ensure we can get a list of Shippers.
#         """
#         url = "/api/v1/shipper/list/"
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_get_shipper_private(self):
#         """
#         Ensure we can get a private list of Shippers.
#         """
#
#         url = "/api/v1/shipper/private/"
#         # self.client.login(username="chaddi", password="wfii123098")
#         self.client.force_login(user)
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


@pytest.mark.django_db
def test_shipper_list(client, auth_client):
    """
    Ensure that anybody can get a list of Shippers.
    """
    response = client.get(url)
    auth_response = auth_client.get(private_url)
    non_auth_response = client.get(private_url)

    assert response.status_code == 200
    assert auth_response.status_code == 200
    assert non_auth_response.status_code == 403


@pytest.mark.django_db
def test_shipper_details(client, auth_client):
    """
    Ensure that only authorized can create, update or delete a Shipper.
    Ensure anybody can get details about Shippers.
    """
    payload = dict(name="BMW Shipper",
                   email="bmw.shipper@mail.ru",
                   country="BY",
                   found_year=2001,
                   description="I am the BMW Shipper!")

    auth_post_response = auth_client.post(private_url, payload)
    non_auth_post_response = client.post(private_url, payload)
    data = auth_post_response.data
    data_id = str(Shipper.objects.get(name="BMW Shipper").id)
    assert auth_post_response.status_code == 201
    assert non_auth_post_response.status_code == 403
    assert data["name"] == payload["name"]

    response = client.get(url+data_id+"/")
    auth_response = auth_client.get(private_url+data_id+"/")
    non_auth_response = client.get(private_url+data_id+"/")

    assert response.status_code == 200
    assert auth_response.status_code == 200
    assert non_auth_response.status_code == 403

    updated_payload = dict(name="BMW Autoidea Shipper",
                           email="bmw.shipper@mail.ru",
                           country="BY",
                           found_year=2005,
                           description="I am the BMW Autoidea Shipper!")

    auth_put_response = auth_client.put(private_url+data_id+"/", updated_payload)
    non_auth_put_response = client.put(private_url+data_id+"/", updated_payload)
    updated_data = auth_put_response.data

    assert auth_put_response.status_code == 200
    assert non_auth_put_response.status_code == 403
    assert updated_data["name"] == updated_payload["name"]
    assert updated_data["found_year"] == updated_payload["found_year"]
    assert updated_data["description"] == updated_payload["description"]

    non_auth_delete_response = client.delete(private_url+data_id+"/")
    delete_response = auth_client.delete(private_url+data_id+"/")

    assert non_auth_delete_response.status_code == 403
    assert delete_response.status_code == 204
