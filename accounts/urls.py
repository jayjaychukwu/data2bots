from django.urls import path
from knox import views as know_views

from .views import LoginAPIView, RegisterAPIView

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("logout/", know_views.LogoutAllView.as_view(), name="logout"),
    path("logoutall/", know_views.LogoutAllView.as_view(), name="logoutall"),
]
