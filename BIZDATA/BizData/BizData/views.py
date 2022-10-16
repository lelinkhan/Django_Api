import requests
from django.shortcuts import render
from .models import Client
from . serializers import ClientSerializers
from rest_framework import viewsets

# Create your views here.
def base(request):
    getapi = requests.get('http://127.0.0.1:8000/show/')
    result = getapi.json()
    return render(request, 'base.html',{'result':result})

class ShowClient(viewsets.ModelViewSet):
    queryset = Client.objects.order_by('gross_income').reverse()[:6]
    serializer_class = ClientSerializers


