from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer

# Driver Viewset
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer