from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about,name='about'),
    path('blog/<str:blog_category>/',views.blog,name='blog'),
    path('contact/',views.contact,name='contact'),
    path('blog/<str:blog_category>/<str:blog_title>/',views.blog_post,name='blog_post'),
]