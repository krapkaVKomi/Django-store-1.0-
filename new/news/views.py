from django.shortcuts import render
from django.http import HttpResponse

from .models import News, Category


def index(request):
    news = News.objects.order_by('-created_at')
    # category = Category.title.order_by("id")
    return render(request, 'new/index.html', {'news': news})#, {'category': category})


def about(request):
    return render(request, 'new/about.html')