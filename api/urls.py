from . import views
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token


handler404 = views.custom404
urlpatterns = [
    path('login', obtain_jwt_token),
    path('user', views.UserList.as_view()),
    path('bookList', views.BookList.as_view()),
    path('getRecord', views.RecordList.as_view()),
    # path('getBook')
    # path('createBook'),
]
