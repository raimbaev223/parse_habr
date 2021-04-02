from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Content


def index(request):
    posts = Content.objects.all()
    paginator = Paginator(posts, 20)
    page = request.GET.get('page')
    try:
        content = paginator.page(page)
    except PageNotAnInteger:
        content = paginator.page(1)
    except EmptyPage:
        content = paginator.page(paginator.num_pages)
    return render(request, 'list.html', {'content': content, 'page': page})


def detail(request, id):
    post = get_object_or_404(Content, id=id)
    return render(request, 'single.html', {'post': post})
