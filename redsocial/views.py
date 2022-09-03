from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import PostForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def feed(request):
    posts = Post.objects.all()
    context = { 'posts': posts }
    return render(request, 'social/feed.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'User {username} created success!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = { 'form': form }
    return render(request, 'social/register.html', context)

@login_required
def post(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'Posted!')
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'social/post.html', { 'form': form})

def deletePost(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('feed')
    

def profile(request, username=None):
    curren_user = request.user
    if username and username != curren_user:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = curren_user.posts.all()
        user = curren_user
    return render(request, 'social/profile.html', { 'user': user, 'posts': posts })

def follow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user
    rel = Relationship(from_user=current_user, to_user=to_user_id)
    rel.save()
    messages.success(request, f'Follow {username}')
    return redirect('feed')

def unfollow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user.id
    rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
    rel.delete()
    messages.success(request, f'Unfollow {username}')
    return redirect('feed')