from .models import PartsDemand
from .permissions import IsOwnerOrReadOnly
from .serializers import PartsDemandSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions


class PartsDemandList(generics.ListCreateAPIView):
    queryset = PartsDemand.objects.all()
    serializer_class = PartsDemandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PartsDemandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PartsDemand.objects.all()
    serializer_class = PartsDemandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
