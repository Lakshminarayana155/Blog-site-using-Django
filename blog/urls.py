from django.urls import path, include
from . import views

urlpatterns = [
    path('postComment',views.postComment,name="postComment"),    
    path('',views.blogpage,name='blogpage'),
    path('<str:slug>',views.blogpost,name='blogpost'),
]