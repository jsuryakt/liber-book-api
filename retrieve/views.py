from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
class TestView(APIView):

    def get(self, request, *args, **kwargs):
        # qs = Post.objects.all()
        # post = qs.first()
        # # serializer = PostSerializer(qs, many=True)
        # serializer = PostSerializer(post)
        data = { 'name':'Liber', 'Year':2020 }
        return Response(data)