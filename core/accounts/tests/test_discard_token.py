import pytest
from rest_framework.authtoken.models import Token
from django.urls import reverse
from ..models import User
from rest_framework.test import APIClient


@pytest.fixture
def common_user():
    user = User.objects.create_user(
        username="Parsa",
        email="parsa@example.com",
        password="a@/1234567",
        is_verified=True,
    )
    return user


@pytest.fixture
def api_client():
    return APIClient(enforce_csrf_checks=False)


@pytest.mark.django_db
class TestAuthFlow:
    def test_login_and_logout(self, common_user, api_client):
        login_url = reverse("accounts:api-v1:token-login")
        login_data = {
            "username": "Parsa",
            "password": "a@/1234567",
        }
        login_response = api_client.post(login_url, login_data)
        assert login_response.status_code == 200
        assert "token" in login_response.data

        token_key = login_response.data["token"]

        logout_url = reverse("accounts:api-v1:token-logout")
        api_client.credentials(HTTP_AUTHORIZATION=f"Token {token_key}")
        logout_response = api_client.post(logout_url)

        assert logout_response.status_code == 204
        assert not Token.objects.filter(user=common_user).exists()

    def test_logout_without_auth(self, api_client):
        logout_url = reverse("accounts:api-v1:token-logout")
        response = api_client.post(logout_url)
        assert response.status_code == 401
