import pytest


shipper_url = "/api/v1/transaction/shipper/list/"
shipper_private_url = "/api/v1/transaction/shipper/private/"
showroom_url = "/api/v1/transaction/showroom/list/"
showroom_private_url = "/api/v1/transaction/showroom/private/"


@pytest.mark.django_db
def test_transaction_shipper_list(client, auth_client):
    """
    Ensure that anybody can get a list of Shipper Transactions.
    """
    response = client.get(shipper_url)
    auth_response = auth_client.get(shipper_private_url)
    non_auth_response = client.get(shipper_private_url)

    assert response.status_code == 200
    assert auth_response.status_code == 200
    assert non_auth_response.status_code == 403


@pytest.mark.django_db
def test_transaction_showroom_list(client, auth_client):
    """
    Ensure that anybody can get a list of Showroom Transactions.
    """
    response = client.get(showroom_url)
    auth_response = auth_client.get(showroom_private_url)
    non_auth_response = client.get(showroom_private_url)

    assert response.status_code == 200
    assert auth_response.status_code == 200
    assert non_auth_response.status_code == 403
