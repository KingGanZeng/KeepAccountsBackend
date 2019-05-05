from django.contrib import admin
from . models import User
from . models import Book
from . models import SpecialBook
from . models import Record
from . models import Group
from . models import Wish
from . models import RecommendedInfo
from . models import Collection
from . models import RecordRecommend
from . models import Files

admin.site.register(User)
admin.site.register(Book)
admin.site.register(SpecialBook)
admin.site.register(Record)
admin.site.register(Group)
admin.site.register(Wish)
admin.site.register(RecommendedInfo)
admin.site.register(Collection)
admin.site.register(RecordRecommend)
admin.site.register(Files)
