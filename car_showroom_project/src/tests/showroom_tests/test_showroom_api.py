import pytest

from src.showroom.models import Showroom


url = "/api/v1/showroom/list/"
private_url = "/api/v1/showroom/private/"

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


@pytest.mark.django_db
def test_showroom_get(client, auth_client, get_responses):
    """
    Ensure that anybody can get a list of Showrooms.
    """
    assert get_responses(client=client, url=url) == 200
    assert get_responses(client=auth_client, url=private_url) == 200
    assert get_responses(client=client, url=private_url) == 403


@pytest.mark.django_db
@pytest.mark.parametrize("payload", [
    payload,
    payload2
])
def test_showroom_post(payload, client, auth_client, post_responses):
    """
    Ensure that only authorized user can create a Showroom.
    """
    assert post_responses(client=client, url=private_url, payload=payload).status_code == 403
    assert post_responses(client=auth_client, url=private_url, payload=payload).status_code == 201
    assert post_responses(client=auth_client, url=private_url, payload=payload).data["name"] == payload["name"]


@pytest.mark.django_db
def test_showroom_details(client, auth_client, details_responses, post_responses):
    """
    Ensure that anybody can get info about separate Showroom.
    """
    post_responses(client=auth_client, url=private_url, payload=payload)
    assert details_responses(client=client, url=url, model=Showroom, payload=payload) == 200
    assert details_responses(client=auth_client, url=private_url, model=Showroom, payload=payload) == 200
    assert details_responses(client=client, url=private_url, model=Showroom, payload=payload) == 403


@pytest.mark.django_db
def test_showroom_delete(client, auth_client, delete_responses, post_responses):
    """
    Ensure that only authorized user can delete a Showroom.
    """
    post_responses(client=auth_client, url=private_url, payload=payload)
    assert delete_responses(client=client, url=private_url, model=Showroom, payload=payload) == 403
    assert delete_responses(client=auth_client, url=private_url, model=Showroom, payload=payload) == 204


@pytest.mark.django_db
@pytest.mark.parametrize("payload, update_payload", [
    (payload, update_payload),
    (payload2, update_payload2)
])
def test_showroom_put(payload, update_payload, client, auth_client, put_responses, post_responses):
    """
    Ensure that only authorized user can update a Showroom.
    """
    post_responses(client=auth_client, url=private_url, payload=payload)
    assert put_responses(client=client,
                         url=private_url,
                         model=Showroom,
                         payload=payload,
                         update_payload=update_payload) == 403
    assert put_responses(client=auth_client,
                         url=private_url,
                         model=Showroom,
                         payload=payload,
                         update_payload=update_payload) == 200


# @pytest.mark.django_db
# def test_showroom_details(client, auth_client):
#     """
#     Ensure that only authorized can create, update or delete a Showroom.
#     Ensure anybody can get details about Showrooms.
#     """
#     payload = dict(name="BMW Showroom",
#                    country="BY",
#                    found_year=2001,
#                    email="bmw.showroom@mail.ru",
#                    description="I am the BMW Showroom!")
#
#     auth_post_response = auth_client.post(private_url, payload)
#     non_auth_post_response = client.post(private_url, payload)
#     data = auth_post_response.data
#     data_id = str(Showroom.objects.get(name="BMW Showroom").id)
#
#     assert auth_post_response.status_code == 201
#     assert non_auth_post_response.status_code == 403
#     assert data["name"] == payload["name"]
#
#     response = client.get(url+data_id+"/")
#     auth_response = auth_client.get(private_url+data_id+"/")
#     non_auth_response = client.get(private_url+data_id+"/")
#
#     assert response.status_code == 200
#     assert auth_response.status_code == 200
#     assert non_auth_response.status_code == 403
#
#     updated_payload = dict(name="Autoidea",
#                            country="BY",
#                            found_year=2005,
#                            email="bmw.showroom@mail.ru",
#                            description="I am the BMW Autoidea Showroom!")
#
#     auth_put_response = auth_client.put(private_url+data_id+"/", updated_payload)
#     non_auth_put_response = client.put(private_url+data_id+"/", updated_payload)
#     updated_data = auth_put_response.data
#
#     assert auth_put_response.status_code == 200
#     assert non_auth_put_response.status_code == 403
#     assert updated_data["name"] == updated_payload["name"]
#     assert updated_data["found_year"] == updated_payload["found_year"]
#     assert updated_data["description"] == updated_payload["description"]
#
#     non_auth_delete_response = client.delete(private_url+data_id+"/")
#     delete_response = auth_client.delete(private_url+data_id+"/")
#
#     assert non_auth_delete_response.status_code == 403
#     assert delete_response.status_code == 204
