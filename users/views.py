from rest_framework import generics
from .serializers import RegisterSerializer
from .models import CustomUser
from django.shortcuts import render

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer