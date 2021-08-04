from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from app.api.portfolio.serializers import General_infoSerializer, ObjectSerializer
from app.model import General_information, Object


class GeneralInfoCreateAPIView(CreateAPIView):
    serializer_class = General_infoSerializer
    queryset = General_information.objects.all()

    def perform_create(self, serializer):

        if serializer.is_valid():
            serializer.save()
            id = serializer.data.get('id')
            return Response(id, status=status.HTTP_201_CREATED)


class ObjectCreateAPIView(CreateAPIView):
    serializer_class = ObjectSerializer
    queryset = Object.objects.all()

    def perform_create(self, serializer):

        if serializer.is_valid():
            serializer.save()
            id = serializer.data.get('id')
            return Response(id, status=status.HTTP_201_CREATED)