from django.contrib import admin

from .models import Book, Review


class Reviewinline(admin.TabularInline):
    model = Review


class BookAdmin(admin.ModelAdmin):
    inlines = [Reviewinline]
    list_display = ("title", "author", "price")


admin.site.register(Book, BookAdmin)
