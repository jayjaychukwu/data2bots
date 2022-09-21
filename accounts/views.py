from django.contrib.auth import login
from django.http import Http404
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from rest_framework import generics, permissions, status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response

from .models import CustomUser
from .permissions import IsOwner
from .serializers import (
    EditUserDetailsSerializer,
    LoginSerializer,
    RegisterSerializer,
    UserSerializer,
)


# Register Client View
class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )


# Client Login View
class LoginAPIView(KnoxLoginView):
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request, format=None):
        data = request.data
        serializer = AuthTokenSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        return super(LoginAPIView, self).post(request, format=None)


class EditUserDetailsAPIView(generics.GenericAPIView):
    serializer_class = EditUserDetailsSerializer
    permission_classes = (IsOwner,)

    def get_object(self, email):
        try:
            return CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        user = self.get_object(request.user.email)
        serializer = self.serializer_class(user, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
