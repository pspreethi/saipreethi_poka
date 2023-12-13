# Contact_management/urls.py

from django.urls import path
from .views import ContactListView, ContactCreateView, ContactUpdateView, ContactDetailView,ContactDeleteView


app_name = 'contact_management'

urlpatterns = [
    path('', ContactListView.as_view(), name='contact_list'),
    path('new/', ContactCreateView.as_view(), name='contact_create'),
    path('<int:pk>/', ContactDetailView.as_view(), name='contact_detail'),
    path('<int:pk>/edit/', ContactUpdateView.as_view(), name='contact_edit'),
    path('<int:pk>/delete/', ContactDeleteView.as_view(), name='contact_delete'),
]
