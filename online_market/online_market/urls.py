from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Настройка для Swagger и ReDoc
schema_view = get_schema_view(
    openapi.Info(
        title="Online Market API",
        default_version="v1",
        description="Документация API для проекта Online Market",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/v1/products/', include('products.urls')),
    path('api/v1/carts/', include('carts.urls')),

    # DRF Session Authentication (drf-auth)
    path('api/v1/drf-auth/', include('rest_framework.urls')),

    # path('api/v1/product/', include('carts.urls')),
    path('user/', include(('user.urls', 'users'), namespace='users')),
    
    # JWT Authentication Endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Swagger и ReDoc интерфейсы
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
