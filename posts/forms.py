from django import forms
from django.forms import ModelForm

from .models import Post
from .models import Comment


class BookForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description', 'author', 'book', 'image')


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text')
