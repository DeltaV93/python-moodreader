import math

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from generator.serializers import EntrySerializer
from .models import Dictionary, Entry


def index(request):
    return render(request, 'generator/index.html')


def past_moods(request):
    entries = Entry.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    return render(request, 'generator/past_moods.html', {'entries': entries})


def detail_mood(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    return render(request, 'generator/detail_mood.html', {'entry': entry})


@api_view(['GET', 'POST'])
def mood_generator(request):
    """
    List all code mood entries, or create a new mood entry.
    """
    if request.method == 'GET':
        print('get')
        entry = Entry.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
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
    num_to_power = (num ** num) * 4.0
    print(num_to_power)
    power_to_hex = hex(math.ceil(num_to_power))
    power_to_hex = '#%s' % power_to_hex[2:8]
    print(power_to_hex)
    return power_to_hex
