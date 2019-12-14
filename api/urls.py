from django.urls import path

from api.views import PostDetail, PostList

urlpatterns = [
    path('', PostList.as_view(), name='posts_list'),
    path('<int:pk>', PostDetail.as_view(), name='posts_detail')
]