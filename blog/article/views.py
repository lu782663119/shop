from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#定义视图函数
def index(request):
    # 将渲染结果输出到index.html页面
    return render(request,'index.html')

