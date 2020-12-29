from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from retrieve.serializers import BookSerializer
from retrieve.models import Book


class BookView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Book.objects.all()
        serializer = BookSerializer(qs, many=True)
        return Response(serializer.data)
