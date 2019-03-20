import django_filters
from . import models


class UserFilter(django_filters.FilterSet):
    uid = django_filters.CharFilter(field_name=('uid', ))

    class Meta:
        model = models.User
        fields = ['uid', ]
