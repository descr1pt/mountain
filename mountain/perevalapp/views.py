from django.shortcuts import render
from rest_framework import generics
from .models import Pereval
from .serializers import PerevalSerializer


class PerevalAPIView(generics.ListAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
