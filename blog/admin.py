from django.contrib import admin
from .models import Blog, BlogReview, BlogCategory, Favorite

@admin.register(Blog)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'date')
    list_filter = ('category', 'author')
    search_fields = ('title', 'author__username')
    
@admin.register(BlogReview)
class BlogReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'blog_post', 'rating')
    list_filter = ('blog_post__title',)
    search_fields = ('user__username', 'blog_post__title')

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'blog_post')
    list_filter = ('user', 'blog_post__category')
    search_fields = ('user__username', 'blog_post__title')