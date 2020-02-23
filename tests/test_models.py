from terms_of_service_agreements.models import UserData

import pytest


@pytest.mark.django_db
def test_user_count():
    assert UserData.objects.count() == 0