from django import forms

from .models import ContactMessage


class CustomContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['first_name','last_name', 'email', 'phone_number', 'message']

