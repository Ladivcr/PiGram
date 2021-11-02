""" posts views"""

# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
#from django.http import HttpResponse

# Models
from posts.models import Post
# Forms
from posts.forms import PostForm 


@login_required
def list_posts(request): 
    """ list existing posts """
    posts = Post.objects.all().order_by('-created')
    return render(request, 'posts/feed.html', {'posts': posts})

@login_required
def create_post(request):
    """ create new post view"""

    if request.method == 'POST': 
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() # nos creara el nuevo post
            return redirect('feed')

    else: form = PostForm()

    return render(
        request=request,
        template_name="posts/new.html",
        context={
            'form': form, 
            'user': request.user,
            'profile': request.user.profile
        })