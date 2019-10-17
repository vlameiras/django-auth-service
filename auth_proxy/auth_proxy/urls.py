from django.contrib import admin
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

schema_view = get_swagger_view(title='Auth API')


api_urlpatterns = [
    path('accounts/', include('rest_registration.api.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urlpatterns)),
    path(r'api/docs/', schema_view),
    path('api/v1/accounts/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/accounts/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/accounts/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
