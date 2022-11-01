from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserLoginForm
from .models import News
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


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


# detail_view
def show_post(request, post_id):
    news = News.objects.filter(id=post_id)
    return render(request, 'new/detail_view.html', {'news': news})


def about(request):
    return render(request, 'new/about.html')


def post_list(request):
    posts_list = News.objects.all()
    query = request.GET.get('q')
    if query:
        posts_list = News.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        ).distinct()
    paginator = Paginator(posts_list, 2) # 6 posts per page
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts
    }
    return render(request, "new/post-list.html", context)





