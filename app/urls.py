
from django.contrib import admin
from django.urls import path
from .views import blog_view,blog_datail_view

urlpatterns = [
path('',blog_view,name='blog-page'),
path('blog/<int:id>',blog_datail_view,name='blog-detail'),
]
