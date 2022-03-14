from django.shortcuts import render

# Create your views here.
def blogs(request):
    return render(request, 'blogs/blogs.html')

def create_blog(request):
    return render(request, 'blogs/create_blog.html')

def update_blog(request):
    return render(request, 'blogs/update_blog.html')

def delete_blog(request):
    return render(request, 'blogs/delete_blog.html')