from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
    portrait = models.URLField(blank=True)
    uid = models.CharField(max_length=50)
    budget = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    group_id_array = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.uid


class Book(models.Model):
    book_id = models.IntegerField()
    uid = models.CharField(max_length=50)
    book_name = models.CharField(max_length=50)
    book_type = models.TextField()

    def __str__(self):
        return self.book_id


class Record(models.Model):
    record_id = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    uid = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    book_id = models.IntegerField()
    # 记录类型：income或expense
    record_type = models.CharField(max_length=50)
    # 记账类型：food, shopping等
    category = models.CharField(max_length=50)
    money = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.record_id


class Group(models.Model):
    group_id = models.IntegerField()
    uid = models.CharField(max_length=50)
    group_name = models.CharField(max_length=50)
    is_admin = models.BooleanField()

    def __str__(self):
        return self.group_id
