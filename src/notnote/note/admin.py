from models import Note
from django.contrib import admin

class NoteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Note, NoteAdmin)