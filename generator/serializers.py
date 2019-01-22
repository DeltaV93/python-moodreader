from rest_framework import serializers

from .models import Entry


class EntrySerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'entry_title',
            'entry',
            'gradient_color_stop_1',
            'gradient_color_stop_2',
            'gradient_color_stop_3',
            'pub_date',
        )
        model = Entry
