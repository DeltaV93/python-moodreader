=====
MoodReader
=====

MoodReader is a simple Django app to find individuals color mood based on
their words. Each time a word entry is submitted each word is checked
for positive/negative connotation and given a color point based on the power
the word. Positive words get positive(happy) brighter colors, negative(sad) words get darker colors.

1. TODO: Refactor the views & model to save mood entry data to create better test.
2. TODO: Add better UX to the results page by returning their entry & color.
3. TODO: Detailed documentation is in the "docs" directory.

Installation
-----------

````
$ cd sites
$ git clone https://github.com/DeltaV93/python-test.git
$ cd python-test
$ pip install -r requirements.txt
$ python manage.py migrate
````

Run Test
-----------

````
$ python manage.py test generator
````


To Run 
-----------

````
python manage.py runserver 
````

Visit http://127.0.0.1:8000/generator/ to start the MoodReader process.

Visit http://127.0.0.1:8000/admin/ to use any of the CRUD methods for the dictionary DB tables. 



Set up
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

4. Start the server and test things out. 


Endpoints
-----------
````
http://127.0.0.1:8000/generator/mood
````
POST request that takes in the user `entry-mood` and returns `colors-list` to results page  
