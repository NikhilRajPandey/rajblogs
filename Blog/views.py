# UserName - master
# Password - Redh@#44k
from django.shortcuts import render, redirect
from Blog.models import AllBlogs
from math import ceil

Mycategories = ["games","programming"]

def pagination(data,page,no_of_post_one_page):
    # Variables Declaring
    page = int(page)
    no_of_post_one_page = int(no_of_post_one_page)
    start_point = (page-1)*no_of_post_one_page
    endpoint = start_point+no_of_post_one_page
    how_many_page = ceil(len(data)/no_of_post_one_page)
    
    Blogdata = []
    

    i = 0
    while i <= len(data):
        if i < endpoint:
            currentData = data[i]
            Blogdata.append(currentData)
        i = i + 1

    paramsdata = {start_point:endpoint,"Blogs":Blogdata,"ceil":how_many_page}

    return paramsdata

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

def blog(request,blog_category,page):
    if blog_category in Mycategories:
        posts = AllBlogs.objects.filter(category=blog_category).order_by('id')[::-1]

        params = pagination(posts,page,5)
        params['index'] = 'False'
        params['scrollData'] = '0'
        return render(request,'blog/post.html',params)
    else:
        return redirect("index")

def blog_post(request,blog_id,blog_category):
    if blog_category in Mycategories:
        post = AllBlogs.objects.filter(id=blog_id).first()
        print(post)
        params = {"post":post}
        return render(request,'blog/blogpost.html',params)
    return redirect('index')

