from phonebook.models import Entry, Address
from django.contrib import admin

class AddressInline(admin.TabularInline):
    model = Address

class EntryAdmin(admin.ModelAdmin):
    inlines = [AddressInline]

admin.site.register(Entry, EntryAdmin)
