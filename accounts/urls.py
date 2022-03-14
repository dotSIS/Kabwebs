from django.urls import path

from. import views

app_name = 'accounts'

urlpatterns = [
    path('', views.accounts, name="accounts"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('forgot_password/', views.forgot_password, name="forgot_password"),
]