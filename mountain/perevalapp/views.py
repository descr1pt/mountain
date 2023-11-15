from django.shortcuts import render
import django_filters
from rest_framework import generics, viewsets
from .models import Pereval, MyUser, Coord, Images, Level
from rest_framework.response import Response
from .serializers import PerevalSerializer, MyUserSerializer, ImagesSerializer, CoordSerializer, LevelSerializer


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["user_id__email"]

    def partial_update(self, request, *args, **kwargs):
        record = self.get_object()
        if record.status == 'NEW':
            serializer = PerevalSerializer(record, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        'state': '1',
                        'message': 'Изменения внесены успешно'
                    }
                )
            else:
                return Response(
                    {
                        'state': '0',
                        'message': serializer.errors
                    }
                )
        else:
            return Response(
                {
                    'state': '0',
                    'message': f'При данном статусе: {record.get_status_display()}, данные изменить нельзя!'
                }
            )


class MyUserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer


class CoordsViewSet(viewsets.ModelViewSet):
    queryset = Coord.objects.all()
    serializer_class = CoordSerializer


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
