# from django.shortcuts import render
from . import models
from . import serializers
from . import filter
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


class StandardPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = "page"


class UserList(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


# 注册用户信息
class UserInfo(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


# 获取用户数据
class UserDetail(generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    filter_fields = ['uid']


# 新建账本
class BookCreate(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer


# 根据uid获取账本列表
class BookList(generics.ListAPIView):
    queryset = models.Book.objects.all().order_by('-create_timestamp')
    serializer_class = serializers.BookSerializer
    pagination_class = StandardPagination
    filter_fields = ['uid']


# 根据book_id获取账单列表
class RecordList(generics.ListAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.RecordSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ['book_id']



