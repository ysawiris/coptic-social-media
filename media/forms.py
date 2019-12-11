from django import forms
from media.models import Post


class PostForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    class Meta:
        model = Post
        fields = ('content', 'author')
