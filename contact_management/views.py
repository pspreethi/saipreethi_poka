from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Contact
from .forms import ContactForm

# Create your views here.
class ContactListView(ListView):
    model = Contact
    template_name = 'contact_list.html'


class ContactCreateView(CreateView):
    model = Contact
    template_name = 'Contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_management:contact_list')

class ContactUpdateView(UpdateView):
    model = Contact
    template_name = 'contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_management:contact_list')

class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contact_detail.html'