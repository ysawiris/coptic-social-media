from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from media.models import Post
from api.serializers import PostSerializer

class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()[:20]
        data = PostSerializer(posts, many=True).data
        return Response(data)

class PostDetail(APIView):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        data = PostSerializer(post).data
        return Response(data)
