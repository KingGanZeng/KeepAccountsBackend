from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('uid', 'username', 'portrait', 'group_id_array')
        model = models.User


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('book_id', 'uid', 'book_name', 'book_type', 'budget', 'create_timestamp')
        model = models.Book


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('record_id', 'update_timestamp', 'uid',
                  'username', 'book_id', 'category', 'record_type',
                  'money', 'note', 'create_timestamp')
        model = models.Record


class SpecialBookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('s_book_id', 'book', 'book_name', 'book_type', 'budget',
                  'create_timestamp', 'uid', 'username')
        model = models.SpecialBook


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('group_id', 'uid', 'group_name', 'is_admin')
        model = models.Group
