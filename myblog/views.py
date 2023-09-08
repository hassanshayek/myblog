from django.shortcuts import render
from blog.models import Blog

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})