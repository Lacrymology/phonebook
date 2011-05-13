from django import forms
from phonebook.models import Entry, Address

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        exclude = ('user')

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ('entry')
