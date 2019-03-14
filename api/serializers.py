from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('uid', 'username', 'portrait', 'budget', 'group_id_array')
        model = models.User


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('book_id', 'uid', 'book_name', 'book_type')
        model = models.Book


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('record_id', 'date', 'uid', 'username', 'book_id', 'record_type', 'money')
        model = models.Record


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('group_id', 'uid', 'group_name', 'is_admin')
        model = models.Group
