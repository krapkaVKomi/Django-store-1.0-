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


# detail_view
def show_post(request, post_id):
    news = News.objects.filter(id=post_id)
    # return HttpResponse(f"Відображення інформації за id {post_id}")
    return render(request, 'new/detail_view.html', {'news': news})


def about(request):
    return render(request, 'new/about.html')


def register(request):
    return render(request, 'new/register.html')


def login(request):
    return render(request, 'new/login.html')









