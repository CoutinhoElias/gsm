from django.contrib import admin

# Register your models here.
from django.contrib.admin import TabularInline

from gsm.person.models import Person, Contact, FilesDocuments


class InlineContact(TabularInline):
    model = Contact


class InlineDocument(TabularInline):
    model = FilesDocuments


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'id', 'name')
    search_fields = ('id', 'name')
    inlines = [InlineContact, InlineDocument, ]


# @admin.register(Kind)
# class KindAdmin(admin.ModelAdmin):
#     list_display = ('__str__', 'id', 'kind')
#     search_fields = ('id', 'kind')

