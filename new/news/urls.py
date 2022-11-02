from django.urls import path
from .views import *
# urls

urlpatterns = [
    path('about/', about),
    path('post/<int:post_id>/', show_post, name='post'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    #path("post-list/", post_list, name='post_list'),
    path("", post_list, name='post_list')
]
