import pytest

from src.customer.models import Customer


url = "/api/v1/customer/list/"
private_url = "/api/v1/customer/private/"

payload = dict(name="Alexandr",
               surname="Snitko",
               email="alex.sn@mail.ru",
               country="BY",
               sex="MALE",
               age=21,
               license=True)

update_payload = dict(name="Alexandr",
                      surname="Nesnitko",
                      email="alex.sn@mail.ru",
                      country="AO",
                      sex="MALE",
                      age=25,
                      license=True)

payload2 = dict(name="Kirill",
                surname="Test",
                email="kirill.test@gmail.com",
                country="AO",
                sex="FEMALE",
                age=26,
                license=False)

update_payload2 = dict(name="Kirill",
                       surname="NotTest",
                       email="kir.not@test.ru",
                       country="RU",
                       sex="MALE",
                       age=29,
                       license=True)


@pytest.mark.django_db
def test_customer_get(client, auth_client, get_responses):
    """
    Ensure that anybody can get a list of Customers.
    """
    assert get_responses(client=client, url=url) == 200
    assert get_responses(client=auth_client, url=private_url) == 200
    assert get_responses(client=client, url=private_url) == 403


@pytest.mark.django_db
@pytest.mark.parametrize("payload", [
    payload,
    payload2
])
def test_customer_post(payload, client, auth_client, post_responses):
    """
    Ensure that only authorized user can create a Customer.
    """
    assert post_responses(client=client, url=private_url, payload=payload).status_code == 403
    assert post_responses(client=auth_client, url=private_url, payload=payload).status_code == 201
    assert post_responses(client=auth_client, url=private_url, payload=payload).data["name"] == payload["name"]


@pytest.mark.django_db
def test_customer_details(client, auth_client, details_responses, post_responses):
    """
    Ensure that anybody can get info about separate Customer.
    """
    post_responses(client=auth_client, url=private_url, payload=payload)
    assert details_responses(client=client, url=url, model=Customer, payload=payload) == 200
    assert details_responses(client=auth_client, url=private_url, model=Customer, payload=payload) == 200
    assert details_responses(client=client, url=private_url, model=Customer, payload=payload) == 403


@pytest.mark.django_db
def test_customer_delete(client, auth_client, delete_responses, post_responses):
    """
    Ensure that only authorized user can delete a Customer.
    """
    post_responses(client=auth_client, url=private_url, payload=payload)
    assert delete_responses(client=client, url=private_url, model=Customer, payload=payload) == 403
    assert delete_responses(client=auth_client, url=private_url, model=Customer, payload=payload) == 204


@pytest.mark.django_db
@pytest.mark.parametrize("payload, update_payload", [
    (payload, update_payload),
    (payload2, update_payload2)
])
def test_customer_put(payload, update_payload, client, auth_client, put_responses, post_responses):
    """
    Ensure that only authorized user can update a Customer.
    """
    post_responses(client=auth_client, url=private_url, payload=payload)
    assert put_responses(client=client,
                         url=private_url,
                         model=Customer,
                         payload=payload,
                         update_payload=update_payload) == 403
    assert put_responses(client=auth_client,
                         url=private_url,
                         model=Customer,
                         payload=payload,
                         update_payload=update_payload) == 200
