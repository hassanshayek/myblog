from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')), 
    path('blog/', include('blog.urls')), 
] 