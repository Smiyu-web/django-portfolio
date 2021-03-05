from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Work, Blog
from .serializers import WorkSerializer, BlogSerializer

# Create your views here.
@api_view(['GET'])
def WorkList(request):
    if request.method == 'GET':
        works = Work.objects.all()
        serializer = WorkSerializer(works, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def BlogList(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
