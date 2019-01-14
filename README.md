=====
MoodReader
=====

MoodReader is a simple Django app to find individuals color mood based on
their words. Each time a word entry is submitted each word is checked
for positive/negative connotation and given a color point based on the power
the word. Positive words get positive(happy) brighter colors, negative(sad) words get darker colors.

TODO: Detailed documentation is in the "docs" directory.
TODO: Refactor the views & model to save mood entry data to create better test.
TODO: Add better UX to the results page by returning their entry & color.

Installation
-----------

````
pip install python-test
````

Requirements
-----------
Django 2.1.5 Python 3.7

Usage
-----------

1. Add "generator" to your INSTALLED_APPS setting like this::

````
    INSTALLED_APPS = [
        ...
        'generator',
    ]
````

2. Include the polls URLconf in your project urls.py like this::

````
    path('generator/', include('generator.urls')),
````

3. Run `python manage.py migrate` to create the generator models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to add a word in the dictionary (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/generator/ to start the MoodReader process.

Endpoints
-----------
````
http://127.0.0.1:8000/generator/mood
````
POST request that takes in the user entry and returns colors list to results page  
