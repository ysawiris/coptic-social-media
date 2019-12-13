from django.urls import path
from media.views import NewsFeedListView, PostCreateNewView, ProfileListView


urlpatterns = [
    path('', NewsFeedListView.as_view(), name='media-list-post'),
    path('profile/', ProfileListView.as_view(), name='media-profile-post'),
    path('create_new/', PostCreateNewView.as_view(), name='media-create-new-post'),
]