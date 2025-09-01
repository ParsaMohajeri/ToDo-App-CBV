import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from ..models import User
import jwt
from django.conf import settings
from datetime import datetime, timedelta
from unittest.mock import patch


@pytest.fixture
def common_user():
    user = User.objects.create_user(
        username="Parsa",
        email="parsa@example.com",
        password="a@/1234567",
        is_verified=False,
    )
    return user


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
class TestActivation:
    def test_activation_success(self, api_client, common_user):
        payload = {
            "user_id": common_user.id,
            "exp": datetime.utcnow() + timedelta(minutes=5),
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
        url = reverse("accounts:api-v1:activation", args=[token])
        response = api_client.get(url)
        assert response.status_code == 200
        common_user.refresh_from_db()
        print(response.status_code, response.data)

        assert common_user.is_verified is True

    @patch("accounts.api.v1.views.EmailThread.start")
    def test_activation_resend(self, mock_email, api_client, common_user):
        url = reverse("accounts:api-v1:activation-resend")
        data = {"email": common_user.email, "username": common_user.username}
        response = api_client.post(url, data)
        print(response.status_code, response.data)

        assert response.status_code == 200
        mock_email.assert_called_once()
