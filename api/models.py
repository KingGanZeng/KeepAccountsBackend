from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
    portrait = models.URLField(blank=True)
    uid = models.CharField(max_length=50, unique=True)
    group_id_array = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.uid)


class Record(models.Model):
    record_id = models.AutoField(primary_key=True)
    update_timestamp = models.DateTimeField(auto_now_add=True)
    uid = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    book_id = models.IntegerField()
    record_type = models.CharField(max_length=50)
    money = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.CharField(max_length=45)
    note = models.CharField(max_length=45, blank=True)
    create_timestamp = models.DateTimeField(null=True)

    def __str__(self):
        return self.record_id


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=50)
    book_name = models.CharField(max_length=50)
    book_type = models.CharField(max_length=50)
    note = models.CharField(max_length=50, blank=True)
    budget = models.DecimalField(max_digits=9, null=True, blank=True, decimal_places=2)
    create_timestamp = models.DateTimeField(auto_now_add=True)
    # record = models.ForeignKey(Record, blank=True, null=True,  on_delete=models.CASCADE)

    def __str__(self):
        return str(self.book_id)


class SpecialBook(models.Model):
    s_book_id = models.AutoField(primary_key=True)
    s_book_label = models.CharField(max_length=200)
    uid = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    book_name = models.CharField(max_length=50)
    book_type = models.CharField(max_length=50)
    book = models.ForeignKey(Book, to_field='book_id', blank=True, null=True,  on_delete=models.CASCADE)
    budget = models.DecimalField(max_digits=9, null=True, blank=True, decimal_places=2)
    create_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.s_book_id)



class Group(models.Model):
    group_id = models.IntegerField()
    uid = models.CharField(max_length=50)
    group_name = models.CharField(max_length=50)
    is_admin = models.BooleanField()

    def __str__(self):
        return self.group_id
