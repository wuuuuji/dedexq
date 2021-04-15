from django.http import HttpResponse

from django.shortcuts import render
from .models import Post

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
    # 传参数到templates\blog\index.html
    # 参数模板位置，需要替换的变量
# Create your views here.
