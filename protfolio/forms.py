# forms.py
from django import forms
from .models import Contact
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            # Keep your widgets here as before
            'name': forms.TextInput(attrs={'class': 'control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'control', 'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'class': 'control', 'placeholder': 'Message'}),
        }

    # Add this function to make fields optional
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = False   # <--- This stops the error
        self.fields['name'].required = False    # Optional
        self.fields['message'].required = False # Optional