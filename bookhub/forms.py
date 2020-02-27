from .models import Post
from django import forms

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title","image","user","description"]
        