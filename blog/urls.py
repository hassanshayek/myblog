from django.urls import path
from . import views

urlpatterns = [
    path('blog_list/', views.blog_list, name='blog_list'), 
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),

    path('create_blog/', views.create_blog, name='create_blog'),
    path('edit_blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('delete_blog/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    
    path('save_favorite/', views.favorite_blogs, name='favorite_blogs'),
    path('blog/save_favorite/<int:blog_id>/', views.save_favorite, name='save_favorite'),
    
    path('author_profile/<int:author_id>/', views.view_author_profile, name='view_author_profile'),
    path('search_blogs/', views.blog_search, name='blog_search'),
    
    path('category/<int:category_id>/', views.blog_by_category, name='blog_by_category'),
    
    path('leave_review/<int:blog_id>/', views.leave_review, name='leave_review'),
]
