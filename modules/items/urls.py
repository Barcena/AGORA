from django.urls import path


from .views import (
    ItemCreateView,
    ItemDetailView,
    ItemListView,
    ItemUpdateView,
)
app_name = 'items'
urlpatterns = [
    path(r'create/',  ItemCreateView.as_view(), name='create'),
    path(r'<int:pk>/edit/', ItemUpdateView.as_view(), name='edit'),
    path(r'<int:pk>/', ItemDetailView.as_view(), name='detail'),
    path(r'', ItemListView.as_view(), name='list'),
]