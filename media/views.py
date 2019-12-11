from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from media.models import Post
from media.forms import PostForm

class PostListView(ListView):
    """ Renders a list of all Post. """
    model = Post

    def get(self, request):
        """ GET a list of Post. """
        posts = self.get_queryset().all()
        return render(request, 'newsfeed.html', {'posts': posts})

class PostDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Post

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'post.html', {'post': post})


class PostCreateNewView(CreateView):
    def get(self, request):
      content = {'form': PostForm()}
      return render(request, 'create_new.html', content)
  
    def post(self, request):
      form = PostForm(request.POST)
      if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse_lazy('media-list-post'))
      return render(request, 'create_new.html', {'form': form})