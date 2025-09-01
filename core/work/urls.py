from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

# ____________________________________________________________________________________________________
app_name = "work"
urlpatterns = [
    # path('',views.IndexView.as_view(), name = "cbv-index"),
    # path("index/", TaskList.as_view(), name="list-task"),
    path("", views.TaskListView.as_view(), name="task-list"),
    path("<int:pk>/", views.TaskDetailView.as_view(), name="task-detail"),
    path("create/", views.TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/edit/", views.TaskEditView.as_view(), name="task-edit"),
    path("<int:pk>/delete/", views.TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/toggle/", views.toggle_task_status, name="toggle-task"),
    path("api/v1/", include("work.api.v1.urls")),
    # path('go-to-index/',views.RedirectToMaktab.as_view(),name='redirect-to-maktab' ),
]
