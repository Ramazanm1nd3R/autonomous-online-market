from django.shortcuts import render
from rest_framework import viewsets
from common.permissions import IsAuthenticatedUser

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedUser]
