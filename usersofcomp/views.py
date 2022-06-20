from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.
from .filters import CompFilterSet
from .models import CompUsers
from django_filters import rest_framework as filters

from .serializers import WorkerSerializer, WorkerUpdateSerializer


class CompanyViewSet(mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet,):
    queryset = CompUsers.objects.all()

    permission_classes = [IsAuthenticated, ]
    serializer_class = WorkerSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CompFilterSet


    def get_serializer_class(self):
        serializer_class = WorkerSerializer

        if self.action == 'update':
            serializer_class = WorkerUpdateSerializer
        return serializer_class

    def get(self, request):
        queryset = self.get_queryset()
        serializer = WorkerSerializer(queryset, many=True)

        return Response({
            "user": serializer.data,
        })

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        filtered_queryset = self.filter_queryset(self.queryset.all())
        serializer = self.get_serializer(filtered_queryset, many=True)
        return Response(serializer.data)
