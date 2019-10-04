from django.contrib.auth.decorators import login_required

from .models import PartsDemand
from .serializers import PartsDemandSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response


class PartsDemandList(generics.ListCreateAPIView):
    serializer_class = PartsDemandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = []
        if self.request.user.is_anonymous:
            return queryset
        elif self.request.user.username == "Administrador":
            return PartsDemand.objects.all()
        return PartsDemand.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PartsDemandDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PartsDemandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = []
        if self.request.user.is_anonymous:
            return queryset
        elif self.request.user.username == "Administrador":
            return PartsDemand.objects.all()
        return PartsDemand.objects.filter(owner=self.request.user)


class CloseDemand(generics.RetrieveAPIView):
    serializer_class = PartsDemandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = []
        if self.request.user.is_anonymous:
            return queryset
        elif self.request.user.username == "Administrador":
            return PartsDemand.objects.all()
        return PartsDemand.objects.filter(owner=self.request.user)

    def get_object(self):
        object = super(CloseDemand, self).get_object()
        object.conclusion_status = True
        object.save()
        return object





class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
