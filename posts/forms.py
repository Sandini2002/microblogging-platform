from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image']  # Ensure 'image' is included
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'What’s on your mind?', 'class': 'form-control'}),
        }
        labels = {
            'content': 'Post Content',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a comment...', 'class': 'form-control'}),
        }
        labels = {
            'content': 'Comment',
        }