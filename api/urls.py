from . import views
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('login', obtain_jwt_token),
    path('user', views.UserList.as_view()),
    path('getBookList', views.BookList.as_view()),
    path('getRecord', views.RecordList.as_view()),
    path('user/wechat-auth', views.UserDetail.as_view()),
    path('user/create', views.UserInfo.as_view({'post': 'create'})),
    path('createBook', views.BookCreate.as_view({'post': 'create'})),
    # path('getBook')
    # path('createBook'),
]
