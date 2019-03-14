# from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers
from django.http import JsonResponse


class UserList(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


def custom404(request):
    return JsonResponse({
        'error_code': 404,
        'error_msg': 'The resource was not found'
    })

