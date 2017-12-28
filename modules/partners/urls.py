from django.urls import path
from .views import viewPartners
from . import views

app_name = 'partners'

urlpatterns = [
	
	path(r'', views.viewPartners, name='view_partners'),
   
	]