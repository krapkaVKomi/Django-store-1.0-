from django.shortcuts import render
from django.http import HttpResponse

from .models import News


def index(request):
    news = News.objects.order_by('-created_at')

    return render(request, 'new/index.html', {'news': news})


def test(request):
    return HttpResponse('<h1>Test News </1>')