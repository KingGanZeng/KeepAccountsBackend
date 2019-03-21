import django_filters
from . import models


class UserFilter(django_filters.FilterSet):
    uid = django_filters.CharFilter('uid')

    class Meta:
        model = models.User
        fields = ['uid', ]


class RecordFilter(django_filters.rest_framework.FilterSet):
    book_id = django_filters.CharFilter('book_id')
    create_time = django_filters.DateTimeFilter('create_time', lookup_expr='icontains')

    class Meta:
        model = models.Record
        fields = ['book_id', 'create_time']

