import math

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Dictionary, Entry
from .forms import EntryForm


def index(request):
    return render(request, 'generator/index.html')


def past_moods(request):
    entries = Entry.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    return render(request, 'generator/past_moods.html', {'entries': entries})


def detail_mood(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    return render(request, 'generator/detail_mood.html', {'entry': entry})


def new_mood(request):
    form = EntryForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            mood_entry = request.POST['entry']
            color_stops = color_stop_generator(mood_entry)
            entry = form.save(commit=False)
            entry.pub_date = timezone.now()
            entry.gradient_color_stop_1 = color_stops[0]
            entry.gradient_color_stop_2 = color_stops[1]
            entry.gradient_color_stop_3 = color_stops[2]
            entry.save()
            return redirect('generator:detail_mood', pk=entry.pk)
        else:
            return render(request, 'generator/index.html', {'error_message': "There was an error. Please try again.", })


def divide_into_chunks(group):
    num_chunks = math.ceil(len(group) / 3)
    for i in range(0, len(group), num_chunks):
        yield list(group[i:i + num_chunks])


def color_stop_generator(entry):
    entry_to_list = entry.lower().split()
    entry_group_lists = list(divide_into_chunks(entry_to_list))

    print(entry_group_lists)
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
    print(hex(math.ceil(num_to_power)))
    print(power_to_hex)
    return power_to_hex
