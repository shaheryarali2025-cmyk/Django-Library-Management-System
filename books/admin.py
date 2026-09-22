from django.contrib import admin
from .models import Book

# Unregister the model first (if already registered)
try:
    admin.site.unregister(Book)
except admin.sites.NotRegistered:
    pass  # If not registered, ignore

# Register with the new admin settings
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'status')
    list_filter = ('status',)
    actions = ['approve_books']

    def approve_books(self, request, queryset):
        """ Admin can approve books from the admin panel """
        queryset.update(status='approved')
    approve_books.short_description = "Approve selected books"

    def reject_books(self, request, queryset):
        queryset.update(status='rejected')
    reject_books.short_description = "Reject selected books"

admin.site.register(Book, BookAdmin)
