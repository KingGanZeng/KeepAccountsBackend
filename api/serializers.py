from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('uid', 'username', 'portrait')
        model = models.User


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('book_id', 'uid', 'book_name',
                  'book_type', 'budget', 'create_timestamp',
                  'image_url', 'is_shared')
        model = models.Book


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('record_id', 'update_timestamp', 'uid',
                  'username', 'book_id', 'category', 'record_type',
                  'money', 'note', 'create_timestamp')
        model = models.Record


class SpecialBookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('s_book_id', 'book', 'book_name',
                  'book_type', 'budget',
                  'create_timestamp', 'uid')
        model = models.SpecialBook


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('group_info_id', 'group_id', 'uid', 'username', 'is_admin', 'portrait')
        model = models.Group


class WishSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('wish_id', 'uid', 'wish_name',
                  'end_time', 'wish_first_category', 'wish_second_category',
                  'money', 'note', 'weight', 'is_finished',
                  'create_timestamp', 'update_timestamp')
        model = models.Wish


class RecommendedInfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('info_id', 'info_name', 'info_content',
                  'climb_url', 'create_timestamp',
                  'first_category', 'second_category')
        model = models.RecommendedInfo


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('info_id', 'collection_id', 'create_timestamp', 'uid')
        model = models.Collection

