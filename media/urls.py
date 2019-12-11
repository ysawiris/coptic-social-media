from django.urls import path
from media.views import PostListView, PostDetailView, PostCreateNewView


urlpatterns = [
    path('', PostListView.as_view(), name='media-list-post'),
    path('create_new/', PostCreateNewView.as_view(), name='media-create-new-post'),
    path('<str:slug>/', PostDetailView.as_view(), name='media-details-post'),
]