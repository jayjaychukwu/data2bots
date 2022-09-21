from django.urls import path
from knox import views as know_views

from .views import EditUserDetailsAPIView, LoginAPIView, RegisterAPIView

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("update/", EditUserDetailsAPIView.as_view(), name="update"),
    path("logout/", know_views.LogoutAllView.as_view(), name="logout"),
    path("logoutall/", know_views.LogoutAllView.as_view(), name="logoutall"),
]
