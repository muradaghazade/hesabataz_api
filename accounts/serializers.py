from rest_framework.serializers import ModelSerializer

from accounts.models import User, Income, Expence, Employee, Invoice, WorkField, Document, DocumentExample, CobsOffer


class InvoiceSerializer(ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class ExpenceSerializer(ModelSerializer):
    class Meta:
        model = Expence
        fields = ('title', 'amount', 'date', 'user')


class IncomeSerializer(ModelSerializer):
    class Meta:
        model = Income
        fields = ('title', 'amount', 'date', 'user')


class SalaryTableSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'salary', 'fin', 'monthly_work_hours', 'work_hours', 'premia', 'vacation', 'life_insurance', 'income_tax', 'pension_fund', 'unemployment_insurance', 'health_insurance',)


class UserSerializer(ModelSerializer):
    incomes = IncomeSerializer(many=True, read_only=True)
    expences = ExpenceSerializer(many=True, read_only=True)
    employes = EmployeeSerializer(many=True, read_only=True)
    class Meta:
        model = User
        exclude = ('username','password','is_superuser', 'is_staff', 'is_active', 'date_joined', 'last_login', 'groups', 'user_permissions',)


class WorkFieldSerializer(ModelSerializer):
    class Meta:
        model = WorkField
        fields = '__all__'


class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class DocumentExampleSerializer(ModelSerializer):
    class Meta:
        model = DocumentExample
        fields = '__all__'


class CobsOfferSerializer(ModelSerializer):
    class Meta:
        model = CobsOffer
        fields = '__all__'