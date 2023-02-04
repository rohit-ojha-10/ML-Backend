from django.shortcuts import render
import requests
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.db import transaction
# Create your views here.
def api_home(request,*args,**kwargs):
    return JsonResponse({'message' : 'hello i am api_home'})

class ListUsers(APIView):
    
    @transaction.atomic
    def get(self, request):
        return JsonResponse({'message' : 'hello i am request'})
    @transaction.atomic
    def post(self,request):
        data = request.data
        print(data)
        return JsonResponse({"hello" : "me" })
