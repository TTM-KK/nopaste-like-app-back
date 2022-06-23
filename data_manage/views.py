from django.shortcuts import get_object_or_404, render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

from .serializer import TextSerializer
from .models import TextData
# Create your views here.

class TextPostAPI(APIView):
    parser_classes = [JSONParser]

    def post(self, request):
        print('sending data', request.data)
        serializer = TextSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class TextGetAPI(APIView):
    def get(self, request, id):
        nopaste = get_object_or_404(TextData, id=id)
        serializer = TextSerializer(instance=nopaste)
        return Response(serializer.data, status.HTTP_200_OK)