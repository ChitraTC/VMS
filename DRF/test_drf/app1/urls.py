
from django.urls import path
from .views import RegisterAPI, RegistrationView, LoginView, LoginAPI

urlpatterns = [
    # path('register/',RegisterAPI.as_view(),name="register"),
    path('register/',RegistrationView.as_view(),name="register"),
    path('login/',LoginView.as_view(),name="login"),
    path('signin/',LoginAPI.as_view(),name="signin")
]