from rest_framework import serializers
from .models import Work, Blog

class WorkSerializer(serializers.ModelSerializer):
  class Meta:
    model = Work
    fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
  class Meta:
    model = Blog
    fields = '__all__'