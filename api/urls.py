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
    path('getAllBookItemRecords', views.AllBookItemRecordList.as_view()),
    # 特殊账本相关API
    path('createSpecialBook', views.SpecialBookCreate.as_view({'post': 'create'})),
    path('getSpecialBookList', views.SpecialBookList.as_view()),
    path('changeSpecialBook/<int:s_book_id>', views.SpecialBookDetail.as_view()),
    path('addSpecialBookItem', views.SpecialBookUpdate.as_view()),
    # 小组相关API
    path('createGroupMember', views.GroupCreate.as_view({'post': 'create'})),
    path('getGroupMembers', views.GroupList.as_view()),
    path('changeGroupMember/<int:group_info_id>', views.GroupDetail.as_view()),
    # 愿望相关API
    path('createWish', views.WishCreate.as_view({'post': 'create'})),
    path('getWishList', views.WishList.as_view()),
    path('changeWish/<int:wish_id>', views.WishDetail.as_view()),
    # 推荐信息获取API
    path('getRecommendInfoList', views.RecommendInfoList.as_view()),
    # 收藏相关API
    path('createCollection', views.CollectionCreate.as_view({'post': 'create'})),
    path('getCollectionList', views.CollectionList.as_view()),
    path('changeCollection<int:collection_id>', views.CollectionDetail.as_view()),
    path('editCollectionItem', views.CollectionUpdate.as_view()),
    # 获取推荐账单模板
    path('getRecordRecommendList', views.RecordRecommendObj.as_view()),
    # 上传图片文件
    path('uploadImageFile', views.FileUpload.as_view()),
]