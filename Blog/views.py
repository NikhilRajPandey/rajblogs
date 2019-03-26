from django.shortcuts import render
from Blog.models import AllBlogs
from random import shuffle
shu
def index(request):
    GameBlogs = AllBlogs.objects.filter(category='games').order_by('id')[::-1]
    ProgBlogs = AllBlogs.objects.filter(category='programming').order_by('id')[::-1]
    params = {"gameBlogs": GameBlogs[0:3],
    "ProgBlogs":ProgBlogs[0:2],"scrollData":400,"index":"True"}

    return render(request,"blog/index.html",params)

def about(request):
    return render(request,'blog/about.html')

def contact(request):
    return render(request,'blog/contact.html')

def blog(request):
    params = {"scrollData":10,"index":"False"}
    return render(request,'blog/post.html',params)

def blog_post(request,blog_title):
    return render(request,'blog/post.html')

