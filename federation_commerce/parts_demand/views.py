from .models import PartsDemand
from .serializers import PartsDemandSerializer
from rest_framework import generics


class PartsDemandList(generics.ListCreateAPIView):
    queryset = PartsDemand.objects.all()
    serializer_class = PartsDemandSerializer


class PartsDemandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PartsDemand.objects.all()
    serializer_class = PartsDemandSerializer