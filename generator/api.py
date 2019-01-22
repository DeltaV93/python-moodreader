import math

from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone

from .models import Entry, Dictionary
from .serializers import EntrySerializer


class MoodView(generics.ListAPIView):
    queryset = Entry.objects.all().order_by('pub_date')
    serializer_class = EntrySerializer


@api_view(['GET', 'POST'])
def mood_generator(request):
    """
    List all code mood entries, or create a new mood entry.
    """
    if request.method == 'GET':
        print('get')
        entry = Entry.objects.all().order_by('pub_date')
        serializer = EntrySerializer(entry, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            mood_entry = serializer.validated_data['entry']
            color_stops = color_stop_generator(mood_entry)
            serializer.validated_data['pub_date'] = timezone.now()
            serializer.validated_data['gradient_color_stop_1'] = color_stops[0]
            serializer.validated_data['gradient_color_stop_2'] = color_stops[1]
            serializer.validated_data['gradient_color_stop_3'] = color_stops[2]
            print('POST')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def divide_into_chunks(group):
    num_chunks = math.ceil(len(group) / 3)
    for i in range(0, len(group), num_chunks):
        yield list(group[i:i + num_chunks])


def color_stop_generator(entry):
    entry_to_list = entry.lower().split()
    entry_group_lists = list(divide_into_chunks(entry_to_list))

    color_points_list = []
    hex_color_list = []
    i = 0

    while i < len(entry_group_lists):
        for word in entry_group_lists[i]:
            try:
                db_lookup = Dictionary.objects.get(word=word)
            except Dictionary.DoesNotExist:
                get_color_point = 0
            else:
                get_color_point = db_lookup.word_value
            color_points_list.append(get_color_point)

        group_sum = sum(num for num in color_points_list)
        hex_color_list.append(num_to_hex(group_sum))
        i += 1
    return hex_color_list


def num_to_hex(num):
    num_to_power = (num ** num) * 5.0
    power_to_hex = hex(math.ceil(num_to_power))
    power_to_hex = '#%s' % power_to_hex[2:8]
    return power_to_hex
