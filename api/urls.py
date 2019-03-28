from . import views
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    # 用户信息API
    path('login', obtain_jwt_token),
    path('user', views.UserList.as_view()),
    path('user/create', views.UserInfo.as_view({'post': 'create'})),
    path('user/wechat-auth', views.UserDetail.as_view()),
    # 账本相关API
    path('createBook', views.BookCreate.as_view({'post': 'create'})),
    path('getBookList', views.BookList.as_view()),
    path('bookChangeApi/<int:book_id>', views.BookDetail.as_view()),
    # 账单流水API
    path('recordDataApi', views.RecordList.as_view({'post': 'create', 'get': 'list'})),
    path('recordChangeApi/<int:record_id>', views.RecordDetail.as_view()),
    # 特殊账本相关API
    path('createSpecialBook', views.SpecialBookCreate.as_view({'post': 'create'})),
    path('getSpecialBookList', views.SpecialBookList.as_view()),
    path('changeSpecialBook/<int:s_book_id>', views.SpecialBookDetail.as_view()),
    path('addSpecialBookItem', views.SpecialBookUpdate.as_view())
]