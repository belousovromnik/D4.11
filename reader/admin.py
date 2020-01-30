from django.contrib import admin
from reader.models import Reader

# Register your models here.

@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_year', 'comment')
    fields = ('full_name', 'birth_year', 'comment')