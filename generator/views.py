import math
from random import randint

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Dictionary

#
# class IndexView(request):
#     return get
def index(request):
    return render(request, 'generator/index.html')


def generate_mood(request):
    mood_entry = request.POST['mood-entry']
    mood_entry_list = mood_entry.lower().split()
    mood_list_length = len(mood_entry_list)
    num_words_per_group = math.ceil(mood_list_length/3)
    color_points_list = []
    # find color point in db
    for w in mood_entry_list:
        try:
            db_lookup = Dictionary.objects.get(word=w)
            get_color_point = db_lookup.word_value
            color_points_list.append(get_color_point)
        except Dictionary.DoesNotExist:
            # get_color_point = 0
            get_color_point = randint(0, 3)
            color_points_list.append(get_color_point)

    # split color point list into 3 and find sum for each
    def divide_into_chunks(group, num_chunks):
        for i in range(0, len(group), num_chunks):
            yield group[i:i + num_chunks]

    color_list = []

    def group_sum_to_color(list_group):
        for group in list_group:
            group_sum = sum(group)
            sum_to_power = math.pow(group_sum, 5.5)
            power_to_hex = hex(math.ceil(sum_to_power))
            print(power_to_hex[-6:])
            color_list.append(power_to_hex[-6:])


    color_points_groups = list(divide_into_chunks(color_points_list, num_words_per_group))
    group_sum_to_color(color_points_groups)
    print(color_list)

    # print(' '.join(z))
    # turn sum into hex color & pass back to UI

    # pprint.pprint(list(list_chunk(mood_entry_list, num_words_per_group)))
    return render(request, 'generator/mood.html', {"color_list": color_list})
