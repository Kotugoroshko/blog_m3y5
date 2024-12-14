from django.shortcuts import render
from blog.models import Post, Author
# Create your views here.
def show_all_posts(request):
    posts = Post.objects.all()
    context = {
        "post_list":posts,
    }
    return render(
        request=request,
        template_name="blog/post_list.html",
        context=context
    )

def post_details_by_id(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        "post":post,
    }
    return render(
        request=request,
        template_name="blog/post_details.html",
        context=context
    )
def show_all_author_posts(request, author_id):
    author = Author.objects.get(id=author_id)
    posts = Post.objects.all().filter(author = author)
    context = {
        
        "posts":posts,
    }
    return render(
        request,
        template_name="blog/author_posts.html",
        context = context
    )