
from django.contrib import admin
from django.urls import include, path
from p_library import views

urlpatterns = [
    path('', views.author_list, name='author_list'),
    path('create', views.AuthorCreate.as_view(), name='author_create'),  
    path('update/<int:pk>/', views.AuthorEdit.as_view(), name='author_update'),
    path('delete/<int:pk>/', views.AuthorDelete.as_view(), name='author_delete'),
]
