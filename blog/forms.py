from django import forms
from .models import Blog, BlogReview 

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body', 'category']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = BlogReview  
        fields = ['rating', 'review_text']
