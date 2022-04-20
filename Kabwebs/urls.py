from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from. import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('accounts/', include('accounts.urls')),
    path('blogs/', include('blogs.urls')),
]

urlpatterns += staticfiles_urlpatterns()