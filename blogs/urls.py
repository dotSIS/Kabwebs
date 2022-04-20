from django.urls import path

from. import views

app_name = 'blogs'

urlpatterns = [
    path('', views.blogs, name="blogs"), # READ
    path('create_blog', views.create_blog, name="create_blog"), # CREATE
    path('update_blog', views.update_blog, name="update_blog"), # UPDATE
    path('delete_blog', views.delete_blog, name="delete_blog"), # DELETE
]