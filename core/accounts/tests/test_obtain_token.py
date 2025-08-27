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
class TestObtainTokenApiView:
    
    def test_login_user_success(self, common_user, api_client):
        url = reverse("accounts:api-v1:token-login")
        data = {
            "username": "Parsa",
            "password": "a@/1234567",
        }
        user=common_user
        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 200

    def test_login_user_password_mismatch(self, common_user, api_client):
        url = reverse("accounts:api-v1:token-login")
        data = {
            "username": "testuser",
            "password": "123",
        }
        user=common_user
        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 400
