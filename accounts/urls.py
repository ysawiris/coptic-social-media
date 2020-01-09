from django.urls import path
from accounts.views import register, ProfileListView, ProfileUpdateView

urlpatterns = [
    path('signup/', register, name='media-signup-page'),
    path('profile/', ProfileListView.as_view(), name='media-profile-post'),
    path('profile/update/', ProfileUpdateView.as_view(), name='update-profile')
]