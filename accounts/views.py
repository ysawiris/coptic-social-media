
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic import CreateView
from media.models import Post
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

    

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') 
            messages.success(request, f'Your account has been created! You are now able to log in')
        return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/signup.html', {'form': form})


class ProfileListView(LoginRequiredMixin, ListView):
    """ Renders a list of all Post. """
    model = Post

    def get(self, request):
        """ GET a list of Post. """
        posts = self.get_queryset().all()
        return render(request, 'profile.html', {'posts': posts}) 