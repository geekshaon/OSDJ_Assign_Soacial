from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):

    return render(request, 'post/home.html')

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post/home.html', {'posts': posts})

@login_required
def create_post(request):
     if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # Handle image upload
        if form.is_valid():
            post = form.save(commit=False)  # Don't save yet, so we can modify the post
            post.user = request.user  # Assign the logged-in user to the post
            post.save()  # Save the post to the database
            messages.success(request, 'Post created successfully!')
            
            return redirect('home')  # Redirect to homepage after saving
        
     else:
         form = PostForm()  # Show an empty form if the request is GET

     return render(request, 'post/create.html', {'form': form})


@login_required
def mypost(request):
    posts = Post.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'post/mypost.html', {'posts': posts})

def postupdate(request, id):
    post = get_object_or_404(Post, id=id)

    # Check if the logged-in user is the owner of the post
    if post.user != request.user:
        messages.error(request, "You are not authorized to edit this post.")
        return redirect('myposts')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully!")
            return redirect('mypost')
    else:
        form = PostForm(instance=post)

    return render(request, 'post/update.html', {'form': form, 'post': post})





def delete_post(request, id):
    post = get_object_or_404(Post, id=id)

    # Ensure only the owner can delete the post
    if post.user != request.user:
        messages.error(request, "You are not authorized to delete this post.")
        return redirect('mypost')

    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post deleted successfully!")
        return redirect('mypost')

    return render(request, 'post/delete.html', {'post': post})
