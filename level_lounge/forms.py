from django import forms
from .models import Comment, Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'parent']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
            'parent': forms.HiddenInput(),  # Hidden input for parent
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'status', 'excerpt']  # Fields to be displayed in the form

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the slug'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the content'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the excerpt'}),
            'status': forms.Select(attrs={'class': 'form-control'}),  # Dropdown for status
        }