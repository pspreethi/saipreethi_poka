# Contact_management/urls.py
from django.urls import path
from .views import ContactListView, ContactCreateView

app_name = 'contact_management'

urlpatterns = [
    path('', ContactListView.as_view(), name='contact_list'),
    path('new/', ContactCreateView.as_view(), name='contact_create'),
]
