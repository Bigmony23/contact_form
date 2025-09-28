from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from contactviews.models import ContactMessage
from .forms import CustomContactForm

# Create your views here.

class ContactView(CreateView):
    model = ContactMessage
    form_class = CustomContactForm
    success_url = reverse_lazy('xabarlar')
    template_name = 'form.html'

class MessageView(ListView):
    model = ContactMessage
    template_name = 'messages.html'
