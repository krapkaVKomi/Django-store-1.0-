from django.urls import path
from .views import *
# urls

urlpatterns = [
    path('about/', about),
    #path('post/<int:post_id>/', show_post, name='post'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path("show_category/<str:category>/", show_category, name='show_category'),
    path("", post_list, name='post_list')
]
