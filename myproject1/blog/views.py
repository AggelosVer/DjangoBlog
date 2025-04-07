from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post



# Create your views here.

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
    return render(request, 'blog/post/detail.html', {'post': post})