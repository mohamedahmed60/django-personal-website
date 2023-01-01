from django.shortcuts import render
from .models import Post
# Create your views here.

def all_posts(requent):
    object = Post.objects.all()
    return render(requent,'blog/post_list.html',{'posts':object})


def post_detail(requent,id):
    object = Post.objects.get(id=id)
    return render(requent,'blog/post_detail.html',{'post':object})
