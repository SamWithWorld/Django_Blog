from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Post,Comment
from .forms import PostForm,CommentForm



def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
    return render(request,'postlist.html',{'posts':posts})


def post_detail(request,pk):
    print pk
    post = get_object_or_404(Post,pk=pk)
    comment = Comment.objects.filter(post__id=pk)


    return render(request,'postdetail.html',{'post':post,'comment':comment})


@login_required()
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog.views.post_detail',pk=post.pk)
    else:
        form = PostForm()
    return render(request,'postnew.html',{'form':form})

@login_required()
def post_edit(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method =='POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('blog.views.post_detail',pk=post.pk)
    else:
        form = PostForm(instance=post)
    return  render(request,'postnew.html',{'form':form})


def add_comment(request,pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post_id = pk
        comment.save()
        return redirect('blog.views.post_detail',pk=pk)




@login_required()
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('-create_date')
    return render(request,'postdraftlist.html',{'posts':posts})

@login_required()
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('blog.views.post_detail',pk=pk)

@login_required()
def post_remove(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.delete()
    return redirect('blog.views.post_list')

def about(request):
    return render(request,'about.html')



