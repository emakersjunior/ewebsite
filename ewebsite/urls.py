"""ewebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path

# usado para mostrar imagens que estao no bd
from django.conf.urls.static import static
from django.conf import settings

# dispara os erros
from django.conf.urls import handler404, handler500

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('contato/', views.contato, name='contato'),
    path('equipe/', views.equipe, name='equipe'),
    path('blog/', views.blog, name='blog'),
    path('blog/resultado/', views.pesquisa_blog, name='pesquisa_blog'),
    path('blog/postagem/<titulo>/', views.blog_post, name='blog_post'), # <titulo> e uma parametro para a view blog_post
    path('blog/<categoria>/', views.blog_categoria, name='blog_categoria'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # usado para mostrar imagens que estao no bd

# trata erros
handler404 = views.error404
handler500 = views.error500