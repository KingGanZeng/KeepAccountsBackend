from django.urls import path
from . import views

handler404 = views.custom404
urlpatterns = [
    path('user', views.UserList.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view()),
]
