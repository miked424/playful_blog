# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
]

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('about/', views.about_view, name='about'),
    path('blog/', views.blog_home, name='blog_home'),
    path('contact-submit/', views.contact_submit, name='contact_submit'),
]