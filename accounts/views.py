from django.shortcuts import redirect, render

# Create your views here.
def accounts_view(request):
    return render(request, 'accounts/accounts.html')

def register_view(request):
    return render(request, 'accounts/register.html')

def login_view(request):
    return render(request, 'accounts/login.html')

def logout_view(request):
    return redirect('blogs:blogs')

def forgot_password(request):
    return render(request, 'accounts/forgot_password.html')