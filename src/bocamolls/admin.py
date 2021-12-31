from django.contrib import admin
from .models import Bocamoll, Subject, Professor

class BocamolltAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['id', 'professor', 'subject', 'text', 'creation', 'approved']

admin.site.register(Bocamoll, BocamolltAdmin)
admin.site.register(Subject)
admin.site.register(Professor)

