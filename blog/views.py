from django.shortcuts import render, get_object_or_404

from .models import Content


def index(request):
    content = Content.objects.all()
    return render(request, 'index.html', {'content': content})


def detail(request, id):
    post = get_object_or_404(Content, id=id)
    return render(request, 'single.html', {'post': post})
