from rest_framework_simplejwt.tokens import AccessToken
import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from ..models import User
from unittest.mock import patch




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
class TestPasswordReset:

    @patch("accounts.api.v1.views.EmailThread.start")
    def test_password_reset_request(self,mock_email, api_client, common_user):
        url = reverse("accounts:api-v1:password-reset-request")
        data = {"email": common_user.email}
        response = api_client.post(url, data)
        assert response.status_code == 200
        mock_email.assert_called_once()





    def test_password_reset_confirm_success(self,api_client, common_user):
        token = str(AccessToken.for_user(common_user))
        url = reverse("accounts:api-v1:password-reset-confirm", args=[token])
        data = {"new_password": "reset/@pass123","new_password1": "reset/@pass123"}
        response = api_client.put(url, data)
        assert response.status_code == 200
        common_user.refresh_from_db()
        assert common_user.check_password("reset/@pass123")
