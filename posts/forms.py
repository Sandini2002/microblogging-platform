from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image']  
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'What’s on your mind?', 'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),  # For image upload
        }
        labels = {
            'content': 'Post Content',
            'image': 'Upload Image',  # Label for the image field
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