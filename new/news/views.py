from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserLoginForm
from .models import News
from django.core.paginator import Paginator
from django.http import HttpResponse


# test
def store(request):
    objects = News.objects.order_by('-created_at')
    paginator = Paginator(objects, 3)
    page_nam = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_nam)
    return render(request, 'new/store.html', {'page_obj': page_objects})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Реєстрація успішна')
            return redirect('/')
        else:
            messages.error(request, 'Помилка реєстрації')
    else:
        form = UserCreationForm()
    return render(request, 'new/register.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = UserLoginForm()
    return render(request, 'new/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('/')


def index(request):
    news = News.objects.order_by('-created_at')
    return render(request, 'new/index.html', {'news': news})


# detail_view
def show_post(request, post_id):
    news = News.objects.filter(id=post_id)
    return render(request, 'new/detail_view.html', {'news': news})


def about(request):
    return render(request, 'new/about.html')


def search(request, find):
    print(find)
    try:
        news = News.objects.filter(title=find)
        return render(request, 'new/search.html', {'news': news})
    except:
        return HttpResponse("<h1>НЕ здавайся</h1>")











