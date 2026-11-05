"""
URL configuration for finalproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),

    path('dashboard/', views.index, name='dashboard'),

    path('register/', views.register, name='register'),

    path('login/', views.user_login, name='login'),

    path('logout/', views.user_logout, name='logout'),

    path('change-password/', views.change_password, name='change_password'),

    path('add_employee/', views.add_employee, name='add_employee'),

    path('single/<int:id>/', views.single_employee, name='single'),

    path('update/<int:id>/', views.update_employee, name='update'),

    path('delete/<int:id>/', views.delete_employee, name='delete'),
]