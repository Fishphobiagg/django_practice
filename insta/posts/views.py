from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    post = Post.objects.all()

    context = {
        'post':post
    }
    return render(request, ('posts/index.html'), context)