from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from blog.models import Post


def about(request):
    return render(request, 'blog/about.html')


def sitemap(request):
    return render(request, 'blog/sitemap.xml')


def blog(request):
    query_results = Post.objects.all().order_by("-date")[:4]
    return render(request, 'blog/blog.html', {'query_results': query_results})


def list_all_posts(request):
    query_results = Post.objects.all().order_by("-date")
    page = request.GET.get('page', 1)
    paginator = Paginator(query_results, 3)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    query_result1 = Post.objects.values('tag').distinct()
    return render(request, 'blog/list_all_posts.html', {'users': users, 'query_result1': query_result1})


def readblog(request, slug):
    query_results = Post.objects.get(slug=slug)
    return render(request, 'blog/post.html', {'query_results': query_results})


