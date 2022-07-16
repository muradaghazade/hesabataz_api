from django.urls import path, include
from accounts.views import UserViewSet, IncomeViewSet, ExpenceViewSet, EmployeeViewSet, SalaryAPIView, InvoiceViewSet
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from .views import *


app_name = 'accounts'

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'income', IncomeViewSet)
router.register(r'expence', ExpenceViewSet)
router.register(r'employee', EmployeeViewSet)
router.register(r'invoice', InvoiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token-data/', DataByTokenView.as_view(), name='token_data'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('salary-table/<int:id>/', SalaryAPIView.as_view(), name='salary-table'),
    path('salary-calculator/', SalaryCalculator.as_view(), name='salary-calculator'),
]
