from .serializers import *
from kekeriders.models import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class KekeriderViewSet(viewsets.ModelViewSet):
    serializer_class = KekeriderSerializer
    queryset = Kekerider.objects.all()
    def get(self, format=None):

        Kekerider = Kekerider.objects.all()
        serializer = SellerSerializer(seller, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SellerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)
