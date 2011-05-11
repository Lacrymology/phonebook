from django import forms
from phonebook.models import Entry

class EntryForm(forms.ModelForm):
    model = Entry
