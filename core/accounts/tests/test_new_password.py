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
        is_verified=True 
    )  
    return user 

@pytest.fixture
def api_client():
    return APIClient()



@pytest.mark.django_db
class TestChangePassword:
    def test_changepassword_successfully(api_client,common_user):
        api_client.force_authenticate(user=common_user)
        url = reverse("accounts:api-v1:change-password")





