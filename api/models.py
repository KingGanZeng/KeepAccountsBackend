from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
    portrait = models.URLField(blank=True)
    uid = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.uid)


class Record(models.Model):
    record_id = models.AutoField(primary_key=True)
    record_type = models.CharField(max_length=50)
    book_type = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=50)
    book_id = models.IntegerField()
    category = models.CharField(max_length=45)
    create_timestamp = models.DateTimeField(null=True)
    update_timestamp = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=45, blank=True)
    money = models.DecimalField(max_digits=9, decimal_places=2)
    uid = models.CharField(max_length=50)

    def __str__(self):
        return str(self.record_id)


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=50)
    book_name = models.CharField(max_length=50)
    book_type = models.CharField(max_length=50)
    note = models.CharField(max_length=50, blank=True)
    image_url = models.CharField(max_length=500, blank=True)
    budget = models.DecimalField(max_digits=9, null=True, blank=True, decimal_places=2)
    create_timestamp = models.DateTimeField(auto_now_add=True)
    is_shared = models.BooleanField(null=True, blank=True)
    # record = models.ForeignKey(Record, blank=True, null=True,  on_delete=models.CASCADE)

    def __str__(self):
        return str(self.book_id)


class SpecialBook(models.Model):
    s_book_id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=50)
    book_name = models.CharField(max_length=50)
    book_type = models.CharField(max_length=50)
    book = models.ManyToManyField(Book, blank=True)
    budget = models.DecimalField(max_digits=9, null=True, blank=True, decimal_places=2)
    create_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.s_book_id)


# 组成员信息
class Group(models.Model):
    group_info_id = models.AutoField(primary_key=True)
    group_id = models.CharField(max_length=50)
    uid = models.CharField(max_length=50)
    username = models.CharField(blank=True, max_length=50)
    portrait = models.URLField(blank=True)
    is_admin = models.BooleanField()

    def __str__(self):
        return self.group_id


# 愿望信息
class Wish(models.Model):
    wish_id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=50)
    wish_name = models.CharField(max_length=50)
    end_time = models.DateTimeField(null=True)
    wish_first_category = models.CharField(max_length=50)
    wish_second_category = models.CharField(max_length=50)
    money = models.DecimalField(max_digits=9, decimal_places=2)
    note = models.CharField(max_length=45)
    weight = models.IntegerField()
    is_finished = models.BooleanField()
    create_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.wish_id)


# 推荐信息存放
class RecommendedInfo(models.Model):
    info_id = models.AutoField(primary_key=True)
    info_name = models.CharField(max_length=50)
    info_content = models.TextField()
    first_category = models.CharField(blank=True, max_length=50)
    second_category = models.CharField(blank=True, max_length=50)
    climb_url = models.URLField(blank=True)
    create_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.info_id)


# 收藏夹
class Collection(models.Model):
    collection_id = models.AutoField(primary_key=True)
    info_id = models.ManyToManyField(RecommendedInfo, blank=True)
    uid = models.CharField(max_length=50)
    create_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.collection_id)


# 账单记录推荐信息
class RecordRecommend(models.Model):
    record_recommend_id = models.AutoField(primary_key=True)
    book_type = models.CharField(max_length=50)
    record_recommend = models.TextField(blank=True)

    def __str__(self):
        return str(self.record_recommend_id)