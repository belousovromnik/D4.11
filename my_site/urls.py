"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from p_library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('index/', views.home),
    path('book/', views.book_list, name='book'),
    path('pubhouse/', views.pubhouse_list, name='pubhouse'),
    path('index/book_increment/', views.book_increment),
    path('index/book_decrement/', views.book_decrement),

    path('author/', views.author_list, name='author_list'),
    path('author/create', views.AuthorCreate.as_view(), name='author_create'),  
    path('author/update/<int:pk>/', views.AuthorEdit.as_view(), name='author_update'),
    path('author/delete/<int:pk>/', views.AuthorDelete.as_view(), name='author_delete'),
    path('author/create_many', views.author_create_many, name='author_create_many'), 

]
