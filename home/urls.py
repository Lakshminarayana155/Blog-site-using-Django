from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('search',views.search,name='search'),
    path('signin',views.blogSignin,name='blogSignin'),
    path('login',views.blogLogin,name='blogLogin'),
    path('logout',views.blogLogout,name='blogLogout'),


]