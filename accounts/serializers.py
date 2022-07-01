from rest_framework.serializers import ModelSerializer

from accounts.models import User, Income, Expence, Employee


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


class UserSerializer(ModelSerializer):
    incomes = IncomeSerializer(many=True, read_only=True)
    expences = ExpenceSerializer(many=True, read_only=True)
    employes = EmployeeSerializer(many=True, read_only=True)
    class Meta:
        model = User
        exclude = ('username','password','is_superuser', 'is_staff', 'is_active', 'date_joined', 'last_login', 'groups', 'user_permissions',)
