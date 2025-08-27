import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from accounts.models import User

@pytest.mark.django_db
class TestRegistrationApiView:
    def test_register_user_success(self):
        client = APIClient()
        url = reverse("accounts:api-v1:registration")  
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "StrongPass123!",
            "password1": "StrongPass123!"
        }
        response = client.post(url, data)
        assert response.status_code == 201
        assert User.objects.filter(email="test@example.com").exists()

    def test_register_user_password_mismatch(self):
        client = APIClient()
        url = reverse("accounts:api-v1:registration")
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "StrongPass123!",
            "password1": "AnotherPass456!"
        }
        response = client.post(url, data)
        assert response.status_code == 400