import pytest
from src.showroom.models import Showroom


url = "/api/v1/showroom/list/"
private_url = "/api/v1/showroom/private/"


@pytest.mark.django_db
def test_showroom_list(client, auth_client):
    """
    Ensure that anybody can get a list of Showrooms.
    """
    response = client.get(url)
    auth_response = auth_client.get(private_url)
    non_auth_response = client.get(private_url)

    assert response.status_code == 200
    assert auth_response.status_code == 200
    assert non_auth_response.status_code == 403


@pytest.mark.django_db
def test_showroom_details(client, auth_client):
    """
    Ensure that only authorized can create, update or delete a Showroom.
    Ensure anybody can get details about Showrooms.
    """
    payload = dict(name="BMW Showroom",
                   country="BY",
                   found_year=2001,
                   email="bmw.showroom@mail.ru",
                   description="I am the BMW Showroom!")

    auth_post_response = auth_client.post(private_url, payload)
    non_auth_post_response = client.post(private_url, payload)
    data = auth_post_response.data
    data_id = str(Showroom.objects.get(name="BMW Showroom").id)

    assert auth_post_response.status_code == 201
    assert non_auth_post_response.status_code == 403
    assert data["name"] == payload["name"]

    response = client.get(url+data_id+"/")
    auth_response = auth_client.get(private_url+data_id+"/")
    non_auth_response = client.get(private_url+data_id+"/")

    assert response.status_code == 200
    assert auth_response.status_code == 200
    assert non_auth_response.status_code == 403

    updated_payload = dict(name="Autoidea",
                           country="BY",
                           found_year=2005,
                           email="bmw.showroom@mail.ru",
                           description="I am the BMW Autoidea Showroom!")

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
