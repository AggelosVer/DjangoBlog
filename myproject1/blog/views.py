from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import EmailPostForm
from django.core.mail import send_mail
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# @login_required
# def post_comment(request, post_id):
#     post = get_object_or_404(Post, id=post_id)

#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             new_comment = form.save(commit=False)
#             new_comment.post = post
#             new_comment.name = request.user.username
#             new_comment.email = request.user.email
#             new_comment.save()
#             return redirect(post.get_absolute_url())  
#     else:
#         form = CommentForm()

#     return render(request, 'blog/comment_form.html', {'form': form, 'post': post})


def post_list(request):
    posts_list = Post.objects.all().order_by('-publish')
    #selidopoihsh
    paginator = Paginator(posts_list, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post/list.html', {'page_obj': page_obj})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )

    new_comment = None
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.name = request.user.username  # pairnei to onoma tou xristi
            new_comment.email = request.user.email    # pairnei to email tou xristi
            new_comment.save()
            form = CommentForm()  
    else:
        form = CommentForm()

    return render(request, 'blog/post/detail.html', {
        'post': post,
        'form': form,
        'new_comment': new_comment,
    })
    return render(request, 'blog/post/detail.html', {'post': post})

def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='P')
    sent = False

    initial_data = {}
    if request.user.is_authenticated:
        initial_data = {
            'name': request.user.username,
            'email': request.user.email
        }

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read '{post.title}'"
            message = f"Read '{post.title}' at {post_url}\n\n{cd['name']}'s comments: {cd['comments']}"
            send_mail(subject, message, cd['email'], [cd['to']])
            sent = True
    else:
        form = EmailPostForm(initial=initial_data)
        
    return render(request, 'blog/post/share.html', {
        'post': post,
        'form': form,
        'sent': sent
    })
