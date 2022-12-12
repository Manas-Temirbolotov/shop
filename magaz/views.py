from django.shortcuts import render
import io
from datetime import datetime
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.forms import model_to_dict
from rest_framework import generics
from rest_framework import viewsets


from .models import Category, Item
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer





