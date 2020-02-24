import pytest

from data import USERS
from terms_of_service_agreements.models import UserData


@pytest.mark.django_db
@pytest.mark.parametrize("first_name, last_name, street, post_code", USERS)
def test_succesful_create_user(first_name, last_name, street, post_code):
    user = UserData.objects.create(first_name=first_name,
                                   last_name=last_name,
                                   street=street,
                                   post_code=post_code)
    assert UserData.objects.first() == user
    return user


@pytest.mark.django_db
@pytest.mark.parametrize("first_name, last_name, street, post_code", USERS)
def test_succesful_remove_user(first_name, last_name, street, post_code):
    user = test_succesful_create_user(first_name, last_name, street, post_code)
    user.delete()
    assert UserData.objects.count() == 0
