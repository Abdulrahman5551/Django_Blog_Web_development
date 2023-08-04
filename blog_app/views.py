from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
# Create your views here.

# last write static fiels get fil css & js & imags
def home(request):
    posts = Post.objects.all()
    countPost = Post.objects.all().count()
    content = {
        'posts': posts,
        'count': countPost,
    }
    return render(request, 'blog/home.html', content)

@login_required
def createPost(request):
    if request.method == "GET":
        context = {
            'form': PostForm(),
        }
        return render(request, 'blog/post_form.html', context)
    
    elif request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
        else:
            return render(request, 'blog/post_form.html', {'form': form})

@login_required
def editPost(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == "GET":
        context = {
            'form': PostForm(instance=post),
            'id': id,
        }
        return render(request, 'blog/post_form.html', context)
    
    elif request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
        
        else:
            return render(request, 'blog/post_form.html', {'form': form})

@login_required
def deletePost(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post,
    }

    if request.method == "GET":
        return render(request, 'blog/delete.html', context) 
    
    elif request.method == "POST":
        post.delete()
        return redirect('home')

def about(request):
    return render(request, 'blog/about.html')