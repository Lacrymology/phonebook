from phonebook.models import Entry
# Create your views here.

# these are not actually views, but rather the functions to
# retrieve the context needed in your views

def getAllEntries():
    return Entry.objects.all()

def getAllNames():
    return map(lambda x: x.name, Entry.objects.all())

def getDefaultData():
    return {'entry_list': getAllEntries()}
