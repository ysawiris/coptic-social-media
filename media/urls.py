from django.urls import path
from media.views import NewsFeedListView, PostCreateNewView


urlpatterns = [
    path('', NewsFeedListView.as_view(), name='media-list-post'),
    path('create_new/', PostCreateNewView.as_view(), name='media-create-new-post'),
]