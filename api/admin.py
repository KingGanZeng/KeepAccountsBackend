from django.contrib import admin
from . models import User
from . models import Book
from . models import Record
from . models import Group

admin.site.register(User)
admin.site.register(Book)
admin.site.register(Record)
admin.site.register(Group)
