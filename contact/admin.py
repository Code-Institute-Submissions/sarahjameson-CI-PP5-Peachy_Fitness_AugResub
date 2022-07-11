from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['contact_date', 'id', 'name']
    list_filter = ('name', 'contact_date')


admin.site.register(Contact, ContactAdmin)
