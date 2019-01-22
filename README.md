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
# add info about making a virtual env. Just to be thorough.
# I got no migrations to apply.
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

// Showing curl commands instead is more accessible.
// Also it says I can use any crud method, but the endpoints only shows POST.

Admin
----
Visit http://127.0.0.1:8000/admin/ to use any of the CRUD methods for the dictionary DB tables.

Login Info

Username: admin 
Password: admin 
 

// The website didn't work for me. Generate Mood didn't work.

Endpoints
-----------
````
http://127.0.0.1:8000/generator/mood
````
POST request that takes in the user `entry-mood` and returns `colors-list` to results page  

//Show an actual post & results example. Are there any other endpoints?
