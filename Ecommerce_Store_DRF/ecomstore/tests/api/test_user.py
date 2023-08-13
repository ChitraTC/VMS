import pytest
from rest_framework.test import APIClient

client = APIClient()

@pytest.mark.django_db
def test_register_user():
    payload = dict(
        # first_name="Harry",
        # last_name="potter",
        email="harry@gmail.com",
        password="Testapi"
    )
    response = client.post("/user/register/",payload)

    data = response.data
    # assert data["first_name"]==payload["first_name"]
    # assert data["last_name"] == payload["last_name"]
    assert data["password"] == payload["password"]
    assert data["email"] == payload["email"]