from django.urls import path
from .views import ListView, AddView, UpdateView, DeleteView, SearchView, generateNewRecords

urlpatterns = [
    path('list/', ListView.as_view(), name='list_view'),
    path('add/', AddView.as_view(), name='add_view'),
    path('get_details/<int:pk>/', UpdateView.as_view(), name='get_details'),
    path('update/', UpdateView.as_view(), name='get_details'),
    path('delete/', DeleteView.as_view(), name='delete_view'),
    path('search/', SearchView.as_view(), name='search_view'),
    path('multiple/', generateNewRecords, name='multiple_records'),
]