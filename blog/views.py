from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Blog, BlogReview, BlogCategory, Favorite
from .forms import BlogForm, ReviewForm 
from django.contrib.auth.models import User 
from django.db.models import Avg
from django.db.models import Q
from django.contrib import messages


@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            category_id = request.POST.get('category')
            new_category_name = request.POST.get('new_category')

            if category_id:
                category = BlogCategory.objects.get(pk=category_id)
            elif new_category_name:
                category, created = BlogCategory.objects.get_or_create(name=new_category_name)

            if category:
                blog = form.save(commit=False)
                blog.author = request.user
                blog.category = category
                blog.save()
                return redirect('blog_list')  
    else:
        form = BlogForm()
    categories = BlogCategory.objects.all()
    return render(request, 'blog/create_blog.html', {'form': form, 'categories': categories})


@login_required
def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id, author=request.user)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_list') 
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/edit_blog.html', {'form': form, 'blog': blog})

@login_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id, author=request.user)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')  
    return render(request, 'blog/delete_blog.html', {'blog': blog})

@login_required
def save_favorite(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    user = request.user

    if not Favorite.objects.filter(user=user, blog_post=blog).exists():
        Favorite.objects.create(user=user, blog_post=blog)
        messages.success(request, "Blog added to favorites.")
    else:
        messages.warning(request, "Blog already in favorites.")
    return redirect('blog_detail', blog_id=blog_id) 



@login_required
def favorite_blogs(request):
    user = request.user
    favorite_blogs = Favorite.objects.filter(user=user).values('blog_post')
    blogs = Blog.objects.filter(id__in=favorite_blogs)

    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/favorite_blogs.html', context)






def view_author_profile(request, author_id):
    author = get_object_or_404(User, id=author_id)
    author_blogs = Blog.objects.filter(author=author)
    return render(request, 'blog/author_profile.html', {'author': author, 'author_blogs': author_blogs})



def blog_search(request):
    query = request.GET.get('q')
    if query:
        blogs = Blog.objects.filter(title__icontains=query)
    else:
        blogs = Blog.objects.none()
    return render(request, 'blog/blog_search_results.html', {'query': query, 'blogs': blogs})


def leave_review(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    reviews = BlogReview.objects.filter(blog_post=blog)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.blog_post = blog
            review.save()
            return redirect('blog_detail', blog_id=blog_id)
    else:
        form = ReviewForm()
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    return render(request, 'blog/leave_review.html', {'form': form, 'blog': blog, 'reviews': reviews, 'average_rating': average_rating})



@login_required
def blog_list(request):
    blogs = Blog.objects.annotate(avg_rating=Avg('blogreview__rating'))
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog/blog_detail.html', {'blog': blog})

#filter blog
def blog_by_category(request):
    blogs = Blog.objects.annotate(avg_rating=Avg('blogreview__rating'))
    if request.GET.get('category_id'):
        blogs = blogs.filter(category_id=request.GET.get('category_id'))
        selected_category = BlogCategory.objects.get(id=request.GET.get('category_id'))
    else:
        blogs = []
        selected_category = None
    context = {
        'blogs': blogs,
        'selected_category': selected_category,
        'categories': BlogCategory.objects.all(),
    }
    return render(request, 'blog/category_filtered_blogs.html', context)





