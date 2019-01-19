from django.contrib import admin

from .models import Dictionary, Entry


class DictionaryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['word']}),
        ('Color Point', {'fields': ['word_value']})
    ]
    list_display = ('word', 'word_value')
    list_filter = ['word']


class EntryAdmin(admin.ModelAdmin):
    fields = [
        'entry_title',
        'entry',
        'gradient_color_stop_1',
        'gradient_color_stop_2',
        'gradient_color_stop_3',
        'pub_date'
    ]
    list_display = [
        'entry_title',
        'gradient_color_stop_1',
        'gradient_color_stop_2',
        'gradient_color_stop_3',
        'pub_date'
    ]


admin.site.register(Dictionary, DictionaryAdmin)
admin.site.register(Entry, EntryAdmin)
