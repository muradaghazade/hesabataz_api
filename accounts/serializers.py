from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from accounts.models import User, Income, Expence, Employee, Invoice, WorkField, Document, DocumentExample, CobsOffer


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('id','email', 'is_taxpayer', 'company_type', 'first_name', 'last_name', 'number', 'password', 'password2')

        def validate(self, attrs):
            if attrs['password'] != attrs['password2']:
                raise serializers.ValidationError({"password": "Password fields didn't match."})

            return attrs


    def create(self, validated_data):
        user = User.objects.create(
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            number = validated_data['number'],
            is_taxpayer = validated_data['is_taxpayer'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user


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