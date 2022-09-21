from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Data2bots API",
        default_version="v1",
        description="An API for Data2bots Assessment",
        terms_of_service="#",
        contact=openapi.Contact(email="odionye.jude@outlook.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # Accounts app url
    path("api/v1/auth/", include("accounts.urls")),
    # Orders app url
    path("api/v1/orders/", include("orders.urls")),
    # Swagger Docs url
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    # Redoc Docs url
    path("redoc", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
