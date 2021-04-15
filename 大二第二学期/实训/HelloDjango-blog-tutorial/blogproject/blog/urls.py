from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>/', views.detail, name='detail'),
    # URL规则<网站域名>/posts/<文章编号>/
    # (int:pk)会将匹配到的数字捕获并作为关键字参数传给detail
    # detail在models.py中运用到
]