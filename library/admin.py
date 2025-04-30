from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'subject', 'added_on')
    search_fields = ('title', 'author', 'subject')
    list_filter = ('subject',)