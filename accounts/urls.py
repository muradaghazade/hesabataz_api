from django.urls import path, include
from accounts.views import UserViewSet, IncomeViewSet, ExpenceViewSet, EmployeeViewSet, SalaryAPIView, InvoiceViewSet, CurrentTaxReference, WorkFieldViewSet, DocumentViewSet, DocumentExampleViewSet, CobsOfferViewSet
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
router.register(r'workfield', WorkFieldViewSet)
router.register(r'document', DocumentViewSet)
router.register(r'document-example', DocumentExampleViewSet)
router.register(r'cobs-offer', CobsOfferViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token-data/', DataByTokenView.as_view(), name='token_data'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('salary-table/<int:id>/', SalaryAPIView.as_view(), name='salary-table'),
    path('salary-calculator/', SalaryCalculator.as_view(), name='salary-calculator'),
    path('current-tax-reference/', CurrentTaxReference.as_view(), name='current-tax-reference'),
    path('second-current-tax-reference/', SecondCurrentTaxReference.as_view(), name='second-current-tax-reference'),
    path('rent-tax/', RentTax.as_view(), name='rent-tax'),
    path('income-tax/', IncomeTax.as_view(), name='income-tax'),
]
