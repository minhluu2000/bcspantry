from django.contrib import admin
from django.urls import path, re_path

from pantry import views

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^$', views.home, name='home'),
    re_path(r'^pantry/(\d+)/', views.pantry_detail, name='pantry_detail'),
]
