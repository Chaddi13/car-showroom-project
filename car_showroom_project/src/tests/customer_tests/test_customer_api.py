import pytest
from src.customer.models import Customer


url = "/api/v1/customer/list/"
private_url = "/api/v1/customer/private/"


@pytest.mark.django_db
def test_customer_list(client, auth_client):
    """
    Ensure that anybody can get a list of Customers.
    """
    response = client.get(url)
    auth_response = auth_client.get(private_url)
    non_auth_response = client.get(private_url)

    assert response.status_code == 200
    assert auth_response.status_code == 200
    assert non_auth_response.status_code == 403


@pytest.mark.django_db
def test_customer_details(client, auth_client):
    """
    Ensure that only authorized can create, update or delete a Customer.
    Ensure anybody can get details about Customers.
    """
    payload = dict(name="Alexandr",
                   surname="Snitko",
                   email="alex.sn@mail.ru",
                   country="BY",
                   sex="MALE",
                   age=21,
                   license=True)

    auth_post_response = auth_client.post(private_url, payload)
    non_auth_post_response = client.post(private_url, payload)
    data = auth_post_response.data
    data_id = str(Customer.objects.get(name="Alexandr").id)

    assert auth_post_response.status_code == 201
    assert non_auth_post_response.status_code == 403
    assert data["name"] == payload["name"]

    response = client.get(url+data_id+"/")
    auth_response = auth_client.get(private_url+data_id+"/")
    non_auth_response = client.get(private_url+data_id+"/")

    assert response.status_code == 200
    assert auth_response.status_code == 200
    assert non_auth_response.status_code == 403

    updated_payload = dict(name="Alexandr",
                           surname="Nesnitko",
                           email="alex.sn@mail.ru",
                           country="AO",
                           sex="MALE",
                           age=25,
                           license=True)

    auth_put_response = auth_client.put(private_url+data_id+"/", updated_payload)
    non_auth_put_response = client.put(private_url+data_id+"/", updated_payload)
    updated_data = auth_put_response.data

    assert auth_put_response.status_code == 200
    assert non_auth_put_response.status_code == 403
    assert updated_data["surname"] == updated_payload["surname"]
    assert updated_data["country"] == updated_payload["country"]
    assert updated_data["age"] == updated_payload["age"]

    non_auth_delete_response = client.delete(private_url+data_id+"/")
    delete_response = auth_client.delete(private_url+data_id+"/")

    assert non_auth_delete_response.status_code == 403
    assert delete_response.status_code == 204
