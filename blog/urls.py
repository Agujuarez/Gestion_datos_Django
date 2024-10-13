from django.urls import path, include
from blog.views import index_view, autor_view

urlpatterns = [
    path('', index_view, name='index'),
    path('autor/<int:id>/', autor_view, name='autor-detail'),
]