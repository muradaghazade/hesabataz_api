from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView 
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from accounts.models import Employee, User, Income, Expence, Invoice, WorkField, Document, DocumentExample, CobsOffer
from accounts.serializers import EmployeeSerializer, UserSerializer, IncomeSerializer, ExpenceSerializer, SalaryTableSerializer, InvoiceSerializer, WorkFieldSerializer, DocumentSerializer, DocumentExampleSerializer, CobsOfferSerializer, UserRegisterSerializer
from django.http import JsonResponse
from rest_framework.generics import CreateAPIView


class RegisterUserAPI(CreateAPIView):
    model = User
    serializer_class = UserRegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        # Wishlist.objects.create(user=user)
        # Cart.objects.create(user=user)


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


class WorkFieldViewSet(viewsets.ModelViewSet):
    queryset = WorkField.objects.all()
    serializer_class = WorkFieldSerializer


class SalaryCalculator(APIView):
    def post(self, request, *args, **kwargs):
        salary = request.POST.get('salary')
        salary = float(salary)+97.68+2.22+8.88
        salary  = "{:.2f}".format(salary)
        return JsonResponse({'salary':salary})


# Hesabat

#Cari vergi arayishi

class CurrentTaxReference(APIView):
    def post(self, request, *args, **kwargs):
        b7 = int(request.POST.get("b7"))
        b8 = int(request.POST.get("b8"))
        b9 = int(request.POST.get("b9"))
        pre_result = b7/b8
        print(pre_result, "1")
        pre_result2 = 100*b9
        print(pre_result2, "2")
        result = pre_result/pre_result2
        print(result)
        return JsonResponse({'result':result})


class SecondCurrentTaxReference(APIView):
    def post(self, request, *args, **kwargs):
        b13 = int(request.POST.get("b13"))
        b14 = int(request.POST.get("b14"))
        pre_result = b13-b14
        result = pre_result*0.05
        print(result)
        return JsonResponse({'result':result})


class RentTax(APIView):
    def post(self, request, *args, **kwargs):
        b4 = int(request.POST.get("b4"))
        b5 = int(request.POST.get("b5"))
        b6 = int(request.POST.get("b6"))
        b7 = b4+b5+b6
        result = b7*0.14
        print(result)
        return JsonResponse({'result':result})


class IncomeTax(APIView):
    def post(self, request, *args, **kwargs):
        b4 = int(request.POST.get("b4"))
        b5 = int(request.POST.get("b5"))
        b6 = int(request.POST.get("b6"))
        b7 = int(request.POST.get("b7"))
        b8 = int(request.POST.get("b8"))
        b9 = int(request.POST.get("b9"))
        b10 = int(request.POST.get("b10"))
        b11 = int(request.POST.get("b11"))
        pre_a12 = b4+b5
        pre2_a12 = b6+b7+b8+b9+b10
        a12 = pre_a12-pre2_a12
        pre_a13 = b6+b7+b8+b9
        pre2_a13 = pre_a13*0.5
        a13 = b4-pre2_a13
        return JsonResponse({'A12':a12, 'A13':a13})


#Sened Numuneleri


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class DocumentExampleViewSet(viewsets.ModelViewSet):
    queryset = DocumentExample.objects.all()
    serializer_class = DocumentExampleSerializer


#Koblarin Teklifi


class CobsOfferViewSet(viewsets.ModelViewSet):
    queryset = CobsOffer.objects.all()
    serializer_class = CobsOfferSerializer