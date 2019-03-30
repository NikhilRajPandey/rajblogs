from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about,name='about'),
    path('blog/<str:blog_category>/<int:page>/',views.blog,name='blog'),
    path('contact/',views.contact,name='contact'),
    path('post/<str:blog_category>/<int:blog_id>/',views.blog_post,name='blog_post'),
]