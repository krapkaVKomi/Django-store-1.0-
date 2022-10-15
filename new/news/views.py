from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import News
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print('ВСЕ УСПІШНО ЗБЕРЕЖЕНО')
            messages.success(request, 'Реєстрація успішна')
            return redirect('login')
        else:
            messages.error(request, 'Помилка реєстрації')
    else:
        form = UserCreationForm()
    return render(request, 'new/register.html', {"form": form})


def index(request):
    news = News.objects.order_by('-created_at')
    category = News.objects.all()
    for i in category:
        print_str = str(i) + 'Властивості' + str(i.categores.all())


    print({'news': news})
    return render(request, 'new/index.html', {'news': news})


# detail_view
def show_post(request, post_id):
    news = News.objects.filter(id=post_id)
    # return HttpResponse(f"Відображення інформації за id {post_id}")
    return render(request, 'new/detail_view.html', {'news': news})


def about(request):
    return render(request, 'new/about.html')


def login(request):
    return render(request, 'new/login.html')









