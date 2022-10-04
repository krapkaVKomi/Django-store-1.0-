from django.shortcuts import render
from django.http import HttpResponse

from .models import News


def index(request):
    news = News.objects.order_by('-created_at')
    category = News.objects.all()
    for i in category:
        print_str = str(i) + 'Властивості' + str(i.categores.all())
        print(print_str)

    print({'news': news})
    return render(request, 'new/index.html', {'news': news})
                                            # id, title, content, category


def about(request):
    return render(request, 'new/about.html')