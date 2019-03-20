# from django.shortcuts import render
from . import models
from . import serializers
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


class StandardPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page"


class UserList(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.CreateModelMixin,
                 viewsets.GenericViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


# 根据uid获取账本列表
class BookList(generics.ListAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ['uid']


# 根据book_id获取账单列表
class RecordList(generics.ListAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.RecordSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ['book_id']



