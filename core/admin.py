from django.contrib import admin
from django_demo.core.models import Entry

class EntryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Entry, EntryAdmin)
