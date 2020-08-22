
from django.contrib import admin
from django.urls import path
from main.views import index # main이라는 앱에 views.py파일에 index라는 함수를 연결
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
] # 사용자가 어떤 url을 쳤는지 어디에 연결되었는지 나타냄. 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)