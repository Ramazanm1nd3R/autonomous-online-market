from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/', include('products.urls')),
    # path('api/v1/', include('carts.urls')),

    path('api/v1/products/', include('products.urls')),
    path('api/v1/carts/', include('carts.urls')),
    # DRF Session Authentication (drf-auth)
    path('api/v1/drf-auth/', include('rest_framework.urls')),

    # path('api/v1/product/', include('carts.urls')),
    path('user/', include('user.urls')),
    # JWT Authentication Endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
