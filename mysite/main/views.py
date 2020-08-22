from django.shortcuts import render
from .models import Post

def index(request):
    postAll = Post.objects.all()
    return render(request, 'main/index.html',
                 {'postAll':postAll})
# index.html에서 파이썬 문법이 들어간 것을 인식하기 위해 render를 쓴다.
