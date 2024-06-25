from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='Project_List'),
    path('projects/create', views.ProjectCreateView.as_view(), name='Project_Create'),
    path('projects/update/<int:pk>', views.ProjectUpdateView.as_view(), name='Project_Update'),
    path('projects/delete/<int:pk>', views.ProjectDeleteView.as_view(), name='Project_Delete'),
    path('tasks/create', views.TaskCreateView.as_view(), name='Task_Create'),
    path('task/update/<int:pk>', views.TaskUpdateView.as_view(), name='Task_Update'),
    path('task/delete/<int:pk>', views.TaskDeleteView.as_view(), name='Task_Delete'),
]