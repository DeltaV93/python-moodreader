from django import forms


from .models import Entry


class EntryForm(forms.ModelForm):

    #TODO: Pep8 cleanup
    class Meta:
        model = Entry
        fields = ('entry_title', 'entry')
