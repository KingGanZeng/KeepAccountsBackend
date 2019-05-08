# from django.shortcuts import render
from django.utils import timezone
from . import models
from . import filter
from . import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


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
    filter_fields = ['uid', 'book_id']


# 更新、删除某一账本
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    lookup_field = 'book_id'


# 根据book_id获取账单列表 || 插入账单信息
class RecordList(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 mixins.UpdateModelMixin,
                 viewsets.GenericViewSet):
    queryset = models.Record.objects.all().order_by('-create_timestamp')
    serializer_class = serializers.RecordSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_class = filter.RecordFilter


# 根据账本id查询项目及账单信息
class AllBookItemRecordList(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        book_id = request.query_params.dict()
        book = models.SpecialBook.objects.filter(s_book_id=book_id['bookId'])
        serialized_book = serializers.SpecialBookSerializer(book, many=True)
        serialized_book = serialized_book.data
        item_list = serialized_book[0]['book']
        record_set = dict()
        # 查询时间为最近一个月
        time_now = timezone.now().strftime("%Y-%m-%d")
        time_past_year = int(time_now.split('-')[0])
        time_past_month = int(time_now.split('-')[1])
        if time_past_month == 1:
            time_past_year = int(time_now.split('-')[0]) - 1
            time_past_month = 12
        time_past_month_now = str(time_past_year) + '-' + str(time_past_month) + '-' + time_now.split('-')[2]

        for item in item_list:
            tmp_item = models.Record.objects.filter(book_id=item, create_timestamp__range=[time_past_month_now, time_now])
            serialized_item = serializers.RecordSerializer(tmp_item, many=True)
            serialized_item = serialized_item.data
            for record_item in serialized_item:
                record_category = record_item['category']
                if record_category in record_set.keys():
                    record_set[record_category] = {
                        'record_type': record_item['record_type'],
                        'usage': record_set[record_category]['usage'] + 1
                    }
                else:
                    record_set[record_category] = {
                        'record_type': record_item['record_type'],
                        'usage': 1
                    }
        record_set = sorted(record_set.items(), key=lambda item: item[1]['usage'], reverse = True)
        return Response({
            'total': len(record_set),
            'record_set': record_set,
        }, status=status.HTTP_200_OK)


# 更新、删除某一账单
class RecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Record.objects.all()
    serializer_class = serializers.RecordSerializer
    lookup_field = 'record_id'


# 新建特殊账本
class SpecialBookCreate(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.SpecialBookSerializer


# 特殊账本查询
class SpecialBookList(generics.ListAPIView):
    queryset = models.SpecialBook.objects.all().order_by('-create_timestamp')
    serializer_class = serializers.SpecialBookSerializer
    pagination_class = StandardPagination
    filter_fields = ['uid', 's_book_id']


# 特殊账本的更新、删除
class SpecialBookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.SpecialBook.objects.all()
    serializer_class = serializers.BookSerializer
    lookup_field = 's_book_id'


# 新增特殊账本项目
class SpecialBookUpdate(APIView):
    def post(self, request):
        data = request.data
        s_book_id = data.get('s_book_id')
        book_id = data.get('book_id')
        special_obj = models.SpecialBook.objects.get(s_book_id=s_book_id)
        book_obj = models.Book.objects.get(book_id=book_id)
        special_obj.book.add(book_obj)
        special_obj.save()
        return Response({'hasAdd': True}, status=status.HTTP_201_CREATED)


# 新建小组成员信息
class GroupCreate(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer


# 根据gid获取组员信息
class GroupList(generics.ListAPIView):
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer
    filter_fields = ['group_info_id', 'uid', 'group_id']


# 更新、删除某一组员信息
class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer
    lookup_field = 'group_info_id'


# 新建愿望信息
class WishCreate(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = models.Wish.objects.all()
    serializer_class = serializers.WishSerializer


# 根据uid获取所有愿望/获取用户某一愿望
class WishList(generics.ListAPIView):
    queryset = models.Wish.objects.all().order_by('is_finished')
    serializer_class = serializers.WishSerializer
    filter_fields = ['uid', 'wish_id']


# 更新、删除某一愿望信息
class WishDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Wish.objects.all()
    serializer_class = serializers.WishSerializer
    lookup_field = 'wish_id'


class InfoPageNumberPagination(PageNumberPagination):
    page_size = 3
    page_query_param = "page"
    page_size_query_param = "page_size"


# 根据info属性查看某条信息
class RecommendInfoList(generics.ListAPIView):
    queryset = models.RecommendedInfo.objects.all()
    serializer_class = serializers.RecommendedInfoSerializer
    pagination_class = InfoPageNumberPagination
    filter_fields = ['info_id', 'first_category', 'second_category']


# 新建收藏信息
class CollectionCreate(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = models.Collection.objects.all()
    serializer_class = serializers.CollectionSerializer


# 根据uid获取所有收藏信息
class CollectionList(generics.ListAPIView):
    queryset = models.Collection.objects.all().order_by('-create_timestamp')
    serializer_class = serializers.CollectionSerializer
    filter_fields = ['uid', 'collection_id']


# 更新、删除某一收藏信息
class CollectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Collection.objects.all()
    serializer_class = serializers.CollectionSerializer
    lookup_field = 'collection_id'


# 新增特殊账本项目
class CollectionUpdate(APIView):
    def post(self, request):
        data = request.data
        collection_id = data.get('collection_id')
        info_id = data.get('info_id')
        collection_obj = models.Collection.objects.get(collection_id=collection_id)
        recommend_obj = models.RecommendedInfo.objects.get(info_id=info_id)
        collection_obj.info_id.add(recommend_obj)
        collection_obj.save()
        return Response({'hasCollected': True}, status=status.HTTP_201_CREATED)

    def delete(self, request):
        data = request.data
        collection_id = data.get('collection_id')
        info_id = data.get('info_id')
        collection_obj = models.Collection.objects.get(collection_id=collection_id)
        recommend_obj = models.RecommendedInfo.objects.get(info_id=info_id)
        collection_obj.info_id.remove(recommend_obj)
        collection_obj.save()
        return Response({'hasDelete': True}, status=status.HTTP_201_CREATED)


# 根据uid获取所有收藏信息
class RecordRecommendObj(generics.ListAPIView):
    queryset = models.RecordRecommend.objects.all()
    serializer_class = serializers.RecordRecommendSerializer
    filter_fields = ['book_type']


class FileUpload(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Files.objects.all()
    serializer_class = serializers.FilesSerializer