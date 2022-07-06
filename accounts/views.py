from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView 
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from accounts.models import Employee, User, Income, Expence, Invoice
from accounts.serializers import EmployeeSerializer, UserSerializer, IncomeSerializer, ExpenceSerializer, SalaryTableSerializer, InvoiceSerializer
from django.http import JsonResponse


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


class ExpenceViewSet(viewsets.ModelViewSet):
    queryset = Expence.objects.all()
    serializer_class = ExpenceSerializer


class DataByTokenView(APIView):
    permission_classes = (IsAuthenticated, )
    def post(self, request, *args, **kwargs):
        user = request.user
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class SalaryAPIView(APIView):
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(Employee, pk=kwargs['id'])
        serializer = SalaryTableSerializer(user)
        return JsonResponse(serializer.data)


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer