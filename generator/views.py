import math

from django.shortcuts import render


from .models import Dictionary


def index(request):
    return render(request, 'generator/index.html')


def generate_mood(request):
    # If you find the need to add inline comments, that's a sign you need a new function.
    # Add documentation http://google.github.io/styleguide/pyguide.html
    mood_entry = request.POST['mood-entry']
    mood_entry_list = mood_entry.lower().split()
    # this variable is not needed, You can use it directly, like math.ceil(len(mood_entry_list))
    mood_list_length = len(mood_entry_list)
    # What is a group? Why are we getting a group of 3
    num_words_per_group = math.ceil(mood_list_length/3)
    color_points_list = []

    # find color point in db
    for w in mood_entry_list:
        try:
            # What is causing the error here? just the db_lookup? I'd take everything out of try/except.
            # When you have alot in try/except it can muddle what is causing the error
            db_lookup = Dictionary.objects.get(word=w)
            get_color_point = db_lookup.word_value
            color_points_list.append(get_color_point)
        except Dictionary.DoesNotExist:
            get_color_point = 0
            # duplicate code
            color_points_list.append(get_color_point)


    color_list = []

    # turn entry color points into hex colors
    # what is this?
    # what is a list_group?
    def group_sum_to_color(list_group):
        # a bunch of for loops here. That adds time calculation. Anyway to combine?
        # Always be thinking about how this would scale.
        for group in list_group:
            group_sum = sum(group)
            sum_to_power = math.pow((group_sum * group_sum * 6), 5.0)
            power_to_hex = hex(math.ceil(sum_to_power))
            color_list.append(power_to_hex[-6:])

    color_points_groups = list(divide_into_chunks(color_points_list, num_words_per_group))
    group_sum_to_color(color_points_groups)
    # turn sum into hex color & pass back to UI
    # This works, but is not RESTful. Generally returning html is more frustrating later on than using JSON and rendering in other ways.
    return render(request, 'generator/mood.html', {"color_list": color_list})


# From the name, I cannot tell what this does.
# I almost never see sub-functions, It's generally separated out like this so it can be called anywhere.
# split color point list into 3 and find sum for each
def divide_into_chunks(group, num_chunks):
    for i in range(0, len(group), num_chunks):
        yield group[i:i + num_chunks]
