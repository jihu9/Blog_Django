from django import forms
from .models import ArticlePost

class ArticlePostForm(forms.ModleForm):
    model = ArticlePost
    fields = ('title', 'body')
