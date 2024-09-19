from django import forms
from .models import Comment, Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    """
    Form for creating comments, linked to the Comment model.
    Includes content and hidden parent fields.
    """
    class Meta:
        model = Comment
        fields = ['content', 'parent']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
            'parent': forms.HiddenInput(),  # Hidden input for parent
        }


class PostForm(forms.ModelForm):
    """
    Form for creating and editing posts, linked to the Post model.
    Includes fields for title, content, status, and excerpt.
    """
    class Meta:
        model = Post
        fields = ['title', 'content', 'status', 'excerpt']  # Fields to be displayed in the form

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the content'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the excerpt'}),
            'status': forms.Select(attrs={'class': 'form-control'}),  # Dropdown for status
        }