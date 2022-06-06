from django.shortcuts import get_object_or_404, render
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from accounts.models import User
from accounts.serializers import UserSerializer




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.request.user.id)
        return obj
    
    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)
