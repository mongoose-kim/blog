from django.contrib import admin

# Register your models here. 블로그 클래스를 불러옴
from .models import Blog

admin.site.register(Blog)
