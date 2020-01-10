from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from media.models import Post
from media.forms import PostForm

class NewsFeedListView(LoginRequiredMixin, ListView):
    """ Renders a list of all Post. """
    model = Post

    def get(self, request):
        """ GET a list of Post. """
        posts = self.get_queryset().all()
        return render(request, 'newsfeed.html', {'posts': posts})


class PostCreateNewView(LoginRequiredMixin, CreateView):
    def get(self, request):
      content = {'form': PostForm()}
      return render(request, 'create_new_post.html', content)
  
    def post(self, request):
      form = PostForm(request.POST)
      if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect(reverse_lazy('media-list-post'))
      return render(request, 'create_new_post.html', {'form': form})