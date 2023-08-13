from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import TaskList, TaskCreate, TaskUpdate, TaskDelete, TaskDetailView, CustomLoginView, RegisterView,send_text_email
from . import views
urlpatterns = [
    path('send_email/',views.send_text_email,name='send_mail'),
    path('login/',CustomLoginView.as_view(),name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    path('logout/',LogoutView.as_view(),name='logout'),

    path('tasklist/',TaskList.as_view(),name='task_list'),
    path('create/',TaskCreate.as_view(),name='task_create'),
    path('update/<int:pk>',TaskUpdate.as_view(),name='task_update'),
    path('delete/<int:pk>',TaskDelete.as_view(),name='task_delete'),
    path('detail/<int:pk>/',TaskDetailView.as_view(),name='task_detail')
]