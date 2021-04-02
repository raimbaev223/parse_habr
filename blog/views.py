from django.shortcuts import render
from .models import Content


def index(request):
    content = Content.objects.first()
    return render(request, 'blog.html', {'content': content})
