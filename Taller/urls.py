from django.contrib import admin
from django.urls import path
from django.urls import include
from blog.views import index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
