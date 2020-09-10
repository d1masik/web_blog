from django.shortcuts import render, get_object_or_404
from .models import Post
from taggit.models import Tag
from django.core.paginator import Paginator


# Create your views here.


def post_list(request, tag_slug=None):
    posts = Post.objects.filter(published=True)
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post/list.html', {'posts': posts, 'tag': tag, 'page_obj': page_obj})


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/post/detail.html', {'post': post})
