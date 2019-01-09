from django.contrib import admin

from .models import Dictionary


class DictionaryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['word']}),
        ('Color Point', {'fields':['word_value']})
    ]
    list_display = ('word', 'word_value')
    list_filter = ['word']


admin.site.register(Dictionary, DictionaryAdmin)