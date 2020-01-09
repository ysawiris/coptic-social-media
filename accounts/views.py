
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView
from media.models import Post
from accounts.models import Profile
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.urls import reverse_lazy

    

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


class ProfileUpdateView(LoginRequiredMixin, CreateView):
    model = Profile
    def get(self, request):
        content = {'form': ProfileUpdateForm()}
        return render(request, 'update_profile.html', content)
    
    def post(self, request):

        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('media-profile-post'))
        return render(request, 'update_profile.html', {'form: form'})
