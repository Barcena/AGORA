from django.urls import path

from . import views
from .views import B2cDetailsView, BusinessCreateView, BusinessUpdateView



app_name = 'business'

urlpatterns = [
	path(r'b2c/register/', views.register, name='register'),
	path(r'b2c/create/', BusinessCreateView.as_view(), name='create'),
	path(r'b2c-profile/', views.view_b2c_profile, name='view_profile'),
    path('<slug:slug>/', views.B2cDetailsView.as_view(), name='detail'),
    path(r'<slug:slug>/edit/', BusinessUpdateView.as_view(), name='edit'),
   ]