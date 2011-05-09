from django.contrib.auth.models import User
from django.db.models import Q
from phonebook.models import Entry
# Create your views here.

# these are not actually views, but rather the functions to
# retrieve the context needed in your views

def getAllEntries(user=None):
    return Entry.objects.filter(Q(user=user) | Q(user=None))

def getAllNames(user=None):
    return Entry.objects.filter(Q(user=user) | Q(user=None)).values_list('first_name', 'last_name')

def getDefaultData(user=None):
    return {'entry_list': getAllEntries(user)}
