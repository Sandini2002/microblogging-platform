# posts/forms.py

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']  # Only allow users to input the post content
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'What’s on your mind?', 'class': 'form-control'}),
        }
        labels = {
            'content': 'Post Content',  # Optional label
        }