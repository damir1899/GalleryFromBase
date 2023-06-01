from django.shortcuts import render
from .models import Category, Post

def index(request):
    Obj_all_post = Post.objects.all()
    return render(request, 'main/index.html', {'context': Obj_all_post})
