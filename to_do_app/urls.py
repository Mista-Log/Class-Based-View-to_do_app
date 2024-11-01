from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task'),
    path('task-edit/<int:pk>/', views.TaskUpdate.as_view(), name='task-edit'),
    path('create-task/', views.TaskCreate.as_view(), name='create-task'),
    path('create-delete/<int:pk>/', views.TaskDelete.as_view(), name='delete-task'),
]
