from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import TaskSerializer
from ...models import Task
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
)
from rest_framework.views import APIView
from rest_framework.generics import (
    GenericAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import mixins
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import DefaultPagination
from django.shortcuts import redirect
import requests
from django.http import JsonResponse
from django.conf import settings



data = {"id": 1, "title": "hello"}


class TaskModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["deadline"]
    search_fields = ["title", "content"]
    ordering_fields = ["deadline"]
    pagination_class = DefaultPagination

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Task.objects.filter(author=user)
        return Task.objects.none()








import requests
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.conf import settings


class WeatherViewSet(viewsets.ViewSet):


    @action(detail=False, methods=['get'])
    def current(self, request):
        city = request.query_params.get("city", "Tehran")
        api_key = settings.OPENWEATHER_API_KEY 
        url = "https://api.openweathermap.org/data/2.5/weather"

        params = {
            "q": city,
            "appid": api_key,
            "units": "metric",
        }

        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code != 200:
            return Response({"error": data.get("message", "something went wrong")}, status=response.status_code)

        result = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
        }
        return Response(result)
