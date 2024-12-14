from django.shortcuts import render
from blog.models import Post
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