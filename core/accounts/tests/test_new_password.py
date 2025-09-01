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
    return APIClient()


@pytest.mark.django_db
class TestChangePassword:
    def test_change_password_success(self, api_client, common_user):
        api_client.force_authenticate(user=common_user)
        url = reverse("accounts:api-v1:change-password")
        data = {
            "old_password": "a@/1234567",
            "new_password": "new!pass/123",
            "new_password1": "new!pass/123",
        }
        response = api_client.put(url, data)
        assert response.status_code == 200
        common_user.refresh_from_db()
        assert common_user.check_password("new!pass/123")

    def test_change_password_wrong_old(self, api_client, common_user):
        api_client.force_authenticate(user=common_user)
        url = reverse("accounts:api-v1:change-password")
        data = {
            "old_password": "wrong",
            "new_password": "new!pass/123",
            "new_password1": "new!pass/123",
        }
        response = api_client.put(url, data)
        print(response.status_code, response.data)

        assert response.status_code == 400

    def test_change_password_unauthenticated(self, api_client):
        url = reverse("accounts:api-v1:change-password")
        data = {
            "old_password": "a@/1234567",
            "new_password": "new!pass/123",
            "new_password1": "new!pass/123",
        }
        response = api_client.put(url, data)
        print(response.status_code, response.data)

        assert response.status_code == 401
