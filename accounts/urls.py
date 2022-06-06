from django.urls import path, include
from accounts.views import UserViewSet
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views


app_name = 'accounts'

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
