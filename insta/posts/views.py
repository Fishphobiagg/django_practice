from django.shortcuts import render, redirect
from .models import Post
from .form import PostForm
# Create your views here.

def index(request):
    post = Post.objects.all()
    context = {
        'post':post
    }
    return render(request, ('posts/index.html'), context)

def create(request):
    print(request)
    print('#'*30)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            pos = form.save()
            return redirect('posts:index')
        return redirect('posts:create')
    else:
        form = PostForm()
    context = {'form':form,}
    return render(request, 'posts/create.html', context)

