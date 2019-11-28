from django.urls import path
from mediapost.views import index 

urlpatterns = [
    path('', index, name="post-hompage" )
]