import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from data import USERS, NOT_VALID_USERS


USER_ENDPOINT = "/api/v1/users/"


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
@pytest.mark.parametrize("first_name, last_name, street, post_code", USERS)
def test_correct_user_data(api_client, first_name, last_name, street, post_code):
    data = {"first_name": first_name,
            "last_name": last_name,
            "street": street,
            "post_code": post_code}
    resp = api_client.post(path=USER_ENDPOINT, data=data, format='json')
    assert resp.status_code == 201


@pytest.mark.django_db
@pytest.mark.parametrize("first_name, last_name, street, post_code", NOT_VALID_USERS)
def test_wrong_user_data(api_client, first_name, last_name, street, post_code):
    data = {"first_name": first_name,
            "last_name": last_name,
            "street": street,
            "post_code": post_code}
    resp = api_client.post(path=USER_ENDPOINT, data=data, format='json')
    assert resp.status_code == 400