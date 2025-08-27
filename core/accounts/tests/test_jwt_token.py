import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from ..models import User


@pytest.fixture
def common_user():
    user = User.objects.create_user(
        username="Parsa",
        email="parsa@example.com",
        password="a@/1234567",
        is_verified=True 
    )  
    return user 

@pytest.fixture
def api_client():
    return APIClient()





@pytest.mark.django_db
class TestTokenObtainPair :
    def test_obtain_token_success(self,api_client, common_user):
        url = reverse("accounts:api-v1:jwt-create")
        data = {"username": "Parsa", "password": "a@/1234567"}
        response = api_client.post(url, data)

        assert response.status_code == 200
        assert "access" in response.data
        assert "refresh" in response.data

    def test_obtain_token_invalid_credentials(self,api_client):
        url = reverse("accounts:api-v1:jwt-create")
        data = {"username": "wrong", "password": "wrongpass"}
        response = api_client.post(url, data)

        assert response.status_code == 401


