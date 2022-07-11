from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    """
    Contact submission form
    """
    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'phone_number',
            'request_call_back',
            'message',
        ]
