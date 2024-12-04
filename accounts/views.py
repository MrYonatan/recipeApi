from django.shortcuts import render
from rest_framework import viewsets
from .models import CustomUser
from rest_framework.permissions import IsAdminUser
from .serializers import CustomUserSerializer
from .permissions import IsAuthorOrReadOnly

class CustomUserViewset(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthorOrReadOnly]
    
    def get_queryset(self):
        if self.request.user.is_staff :
            return CustomUser.objects.all()
        return CustomUser.objects.filter(id=self.request.user.id)
    