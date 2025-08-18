from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
# ____________________________________________________________________________________________________

router=DefaultRouter()
app_name="api-v1"
router.register('task',views.TaskModelViewSet,basename='task')
urlpatterns=router.urls




