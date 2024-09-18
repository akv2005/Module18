"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from sys import platform


from django.contrib import admin
from django.urls import path
from task2.views import class2, func2
#from task3.views import main, cart, games
from task4.views import cart, games, main
from task5.views import sign_up_by_django, sign_up_by_html
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('class/', class2.as_view()),
    path('func/', func2),
#    path('', main.as_view(template_name='third_task/platform.html')),
    path('', TemplateView.as_view(template_name='fourth_task/menu.html')),
    path('cart/', cart),
    path('games/', games),
    path('django_sign_up/', sign_up_by_django),
    path('django_sign/', sign_up_by_html),
]
