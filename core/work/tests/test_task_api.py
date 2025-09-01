import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from accounts.models import User
from ..models import Task
from datetime import date, timedelta


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user():
    return User.objects.create_user(
        username="parsa", email="test234445@gmail.com", password="test/@pass"
    )


@pytest.fixture
def other_user():
    return User.objects.create_user(
        username="other", email="test23444ve5@gmail.com", password="other/@pass"
    )


@pytest.fixture
def task(user):
    return Task.objects.create(
        author=user,
        title="My Task",
        content="Some content",
        deadline=date.today() + timedelta(days=3),
    )


@pytest.mark.django_db
class TestTaskViewSet:
    def test_list_authenticated_user_sees_own_tasks(
        self, api_client, user, task, other_user
    ):
        Task.objects.create(
            author=other_user,
            title="Other Task",
            content="Hidden",
            deadline=date.today(),
        )

        api_client.force_authenticate(user=user)
        url = reverse("work:api-v1:task-list")
        response = api_client.get(url)
        assert response.status_code == 200
        titles = [t["title"] for t in response.data["results"]]
        assert "My Task" in titles
        assert "Other Task" not in titles

    def test_list_unauthenticated_user_gets_empty_queryset(self, api_client, task):
        url = reverse("work:api-v1:task-list")
        response = api_client.get(url)
        assert response.status_code == 403

    def test_create_task_authenticated(self, api_client, user):
        api_client.force_authenticate(user=user)
        url = reverse("work:api-v1:task-list")
        data = {"title": "New Task", "content": "Do something"}
        response = api_client.post(url, data)
        assert response.status_code == 201
        task = Task.objects.get(title="New Task")
        assert task.author == user

    def test_create_task_unauthenticated_fails(self, api_client):
        url = reverse("work:api-v1:task-list")
        data = {"title": "No Auth", "content": "Should fail"}
        response = api_client.post(url, data)
        assert response.status_code == 403

    def test_update_task_by_owner(self, api_client, user, task):
        api_client.force_authenticate(user=user)
        url = reverse("work:api-v1:task-detail", args=[task.id])
