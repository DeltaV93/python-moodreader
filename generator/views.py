import math

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponse


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
    mood_entry = request.POST['entry']
    color_stops = color_stop_generator(mood_entry)
    print(color_stops[0])
    print(color_stops[1])
    print(color_stops[2])
    if request.method == 'POST':
        if form.is_valid():
            entry = form.save(commit=False)
            entry.pub_date = timezone.now()
            entry.gradient_color_stop_1 = color_stops[0]
            entry.gradient_color_stop_2 = color_stops[1]
            entry.gradient_color_stop_3 = color_stops[2]
            entry.save()
        else:
            print('form not valid')
            print(form)

    else:
        print('not a post')
        print(form.errors)
        form = EntryForm()
    return render(request, 'generator/mood.html', {'entry': form})


# From the name, I cannot tell what this does.
# I almost never see sub-functions, It's generally separated out like this so it can be called anywhere.
# split color point list into 3 and find sum for each
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
    num_to_power = math.pow((num * num * 6), 5.0)
    power_to_hex = hex(math.ceil(num_to_power))
    return '#%s' % power_to_hex[-6:]
