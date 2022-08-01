import pytest
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from src.shipper.models import Shipper


url = "/api/v1/shipper/list/"
private_url = "/api/v1/shipper/private/"

payload = dict(name="Test name",
               country="BY",
               found_year=2001,
               email="test@test.ru",
               description="I am the Test description!")

update_payload = dict(name="Put test name",
                      country="BY",
                      found_year=2005,
                      email="put.test@test.ru",
                      description="I am the Put Test description!")

payload2 = dict(name="Test name 2",
                country="AO",
                found_year=2006,
                email="test2@test2.ru",
                description="I am the Test 2 description!")

update_payload2 = dict(name="Put test name 2",
                       country="RU",
                       found_year=2009,
                       email="put.test2@test2.ru",
                       description="I am the Put Test 2 description!")

# class AccountTests(APITestCase):
#     user = ShipperUser.objects.create_user(username='alex', password='wfii123098')
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
def test_shipper_get(client, auth_client, get_responses):
    """
    Ensure that anybody can get a list of Shippers.
    """
    assert get_responses(client=client, url=url) == 200
    assert get_responses(client=auth_client, url=private_url) == 200
    assert get_responses(client=client, url=private_url) == 403


@pytest.mark.django_db
@pytest.mark.parametrize("payload", [
    payload,
    payload2
])
def test_shipper_post(payload, client, auth_client, post_responses):
    """
    Ensure that only authorized user can create a Shipper.
    """
    assert post_responses(client=client, url=private_url, payload=payload).status_code == 403
    assert post_responses(client=auth_client, url=private_url, payload=payload).status_code == 201
    assert post_responses(client=auth_client, url=private_url, payload=payload).data["name"] == payload["name"]


@pytest.mark.django_db
def test_shipper_details(client, auth_client, details_responses, post_responses):
    """
    Ensure that anybody can get info about separate Shipper.
    """
    post_responses(client=auth_client, url=private_url, payload=payload)
    assert details_responses(client=client, url=url, model=Shipper, payload=payload) == 200
    assert details_responses(client=auth_client, url=private_url, model=Shipper, payload=payload) == 200
    assert details_responses(client=client, url=private_url, model=Shipper, payload=payload) == 403


@pytest.mark.django_db
def test_shipper_delete(client, auth_client, delete_responses, post_responses):
    """
    Ensure that only authorized user can delete a Shipper.
    """
    post_responses(client=auth_client, url=private_url, payload=payload)
    assert delete_responses(client=client, url=private_url, model=Shipper, payload=payload) == 403
    assert delete_responses(client=auth_client, url=private_url, model=Shipper, payload=payload) == 204


@pytest.mark.django_db
@pytest.mark.parametrize("payload, update_payload", [
    (payload, update_payload),
    (payload2, update_payload2)
])
def test_shipper_put(payload, update_payload, client, auth_client, put_responses, post_responses):
    """
    Ensure that only authorized user can update a Shipper.
    """
    post_responses(client=auth_client, url=private_url, payload=payload)
    assert put_responses(client=client,
                         url=private_url,
                         model=Shipper,
                         payload=payload,
                         update_payload=update_payload) == 403
    assert put_responses(client=auth_client,
                         url=private_url,
                         model=Shipper,
                         payload=payload,
                         update_payload=update_payload) == 200
