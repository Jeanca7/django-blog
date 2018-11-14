from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone  
from .forms import PostForm
from django.contrib.auth.decorators import login_required #To create a post is required to be logged in ***
from django.contrib.auth.decorators import permission_required

# Create your views here.
def is_in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

def user_can_edit_post(request, post):
    wrote_the_post = post.author == request.user
    is_editor = is_in_group(request.user, 'editors')
    superuser = request.user.is_superuser
    return wrote_the_post or superuser or is_editor


def display_content(request):
    posts = Post.objects.filter(published_date__lte = timezone.now())  
    return render(request, "blog/get_index.html", {'posts': posts}) 

def repost_detail(request, id):
    post = get_object_or_404(Post, pk=id)#I get the post through the primary key
    post.views += 1 #TO FIX ***
    post.save()
    is_editor = request.user.groups.filter(name='editors').exists()
    
    can_edit = user_can_edit_post(request, post)
    
    return render(request, "blog/repost_detail.html", {'post': post, 'can_edit': can_edit})



def edit_post(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method=="POST":
        form = PostForm(request.POST, instance=post)
        form.save()
        return redirect("/")
    else:
        form=PostForm(instance=post)
        return render(request, "blog/edit_post.html", {'form': form})
        

@login_required #login required to write a post***
def write_post(request):
    if request.method=="POST":
        form = PostForm(request.POST, request.FILES) #request data from the form
        post=form.save(commit=False) #I don't save it in the database yet but I save it in the model
        post.author = request.user #I assign the author attribute to the username that i requested  
        post.save() #i save the post in my database
        return redirect(repost_detail, post.id)
    else:
        form=PostForm()
        return render(request, "blog/edit_post.html", {'form': form})
        
@permission_required('blog.can_publish')
def get_unpublished_posts(request):
    posts = Post.objects.filter(published_date__gte = timezone.now())  
    return render(request, "blog/get_index.html", {'posts': posts})

@permission_required('blog.can_publish')
def publish_post(request, id):
    post = get_object_or_404(Post, pk=id)
    post.published_date = timezone.now()
    post.save()
    return redirect(read_post, post.id)