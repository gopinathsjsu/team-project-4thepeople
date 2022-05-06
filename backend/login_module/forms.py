from django import forms
from .models import Customer


# Create your forms here.
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('username', 'password', 'email', 'contact')
