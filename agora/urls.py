"""agora URL Configuration

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
from django.urls import path, include
from django.contrib import admin
from agora import views
from django.conf import settings
from django.conf.urls.static import static

# from todolist.urls import urlpatterns

urlpatterns = [
    path(r'', views.login_redirect, name='login_redirect'),
    path(r'admin/', admin.site.urls),
    path(r'accounts/', include('modules.accounts.urls', namespace='accounts')),
    path(r'home/', include('modules.home.urls', namespace='home')),
    path(r'business/', include('modules.business.urls', namespace='business')),
    path(r'items/', include('modules.items.urls', namespace='items')),
    path(r'todolist/', include('modules.todolist.urls', namespace='todolist')),
    path(r'partners/', include('modules.partners.urls', namespace='partners')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)