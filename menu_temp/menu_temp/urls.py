"""menu URL Configuration."""
from django.contrib import admin
from django.urls import path, include

from tag_menu import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tag_menu.urls')),
    path('', views.index, name='home'),
]
