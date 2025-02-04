"""
URL configuration for MyBlog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import blog.views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("posts/", blog_views.show_all_posts, name="post_list"),
    path("post/<int:post_id>/",blog_views.post_details_by_id, name="post_details"),
    path("author/<int:author_id>/",blog_views.show_all_author_posts, name="author_posts")
]
