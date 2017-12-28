from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path(r'', views.showB2cHome, name='home'),
   
   # url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends')
]