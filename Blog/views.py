from django.shortcuts import render, redirect
from Blog.models import AllBlogs
from math import ceil

def Pagination(data):
    
    pass

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

def blog(request,blog_category):
    Mycategories = ["game","programming"]
    if blog_category in Mycategories:
        posts = AllBlogs.objects.filter(category='games').all()
        
        params = {"scrollData":10,"index":"False"}
        return render(request,'blog/post.html',params)
    else:
        return redirect("index")

def blog_post(request,blog_title):
    return render(request,'blog/post.html')

