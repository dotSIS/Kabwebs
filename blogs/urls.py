from django.urls import path
from. import views

app_name = 'blogs'

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('create/', views.create_blog, name='create'),
    path('<slug>/', views.blog, name='blog'),
]