from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .serializers import TaskSerializer
from ...models import Task
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser,IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView ,ListCreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .paginations import DefaultPagination
from django.shortcuts import redirect
data={
    "id":1,
    "title":"hello"
}


class TaskModelViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    serializer_class=TaskSerializer
    queryset = Task.objects.all()
    filter_backends =[DjangoFilterBackend,SearchFilter,OrderingFilter]    
    filterset_fields = ['deadline']
    search_fields =['title','content']
    ordering_fields= ['deadline']
    pagination_class=DefaultPagination







    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)


    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        return super().dispatch(request, *args, **kwargs)
