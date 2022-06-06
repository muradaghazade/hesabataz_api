from rest_framework.serializers import ModelSerializer

from accounts.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ('password','is_superuser', 'is_staff', 'is_active', 'date_joined', 'last_login', 'groups', 'user_permissions', 'slug')