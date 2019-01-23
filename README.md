=====
MoodReader
=====

MoodReader is a simple Django app to find individuals color mood based on
their words. Each time a word entry is submitted each word is checked
for positive/negative connotation and given a color point based on the power
the word. Positive words get positive(happy) brighter colors, negative(sad) words get darker colors.

1. TODO: Add voting function for each entry
2. TODO: Detailed documentation is in the "docs" directory.

Installation
-----------

````
$ cd sites
$ git clone https://github.com/DeltaV93/python-test.git
$ cd python-test
$ virtualenv env
$ source env/bin/activate
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

Visit http://127.0.0.1:8000/ to start the MoodReader process.

// Showing curl commands instead is more accessible.
// Also it says I can use any crud method, but the endpoints only shows POST.

Admin
----
```
Visit http://127.0.0.1:8000/admin/
``` 

Login Info

Username: admin 
Password: admin 

Once inside admin site you can view, update, & delete items in the Dictionary or Entry DB tables.


API Endpoints
-----------
````
http://127.0.0.1:8000/api
Method: POST
Take: [ 
   {  
      "entry_title": "jimi hendrix sunshine of your love",
      "entry": "It's getting near dawn,When lights close their tired eyes. I'll soon be with you my love, To give you my dawn surprise. I'll be with you darling soon, I'll be with you when the stars start falling. I've been waiting so longTo be where I'm goingIn the sunshine of your love. I'm with you my love, The light's shining through on you. Yes,  I'm with you my love, It's the morning and just we two. I'll stay with you darling now, I'll stay with you till my seas are dried up.",
      "gradient_color_stop_1": "",
      "gradient_color_stop_2": "",
      "gradient_color_stop_3": "",
      "pub_date": ""
   }
]
Returns: [ 
   {  
      "id": 194,
      "entry_title": "jimi hendrix sunshine of your love",
      "entry": "It's getting near dawn,When lights close their tired eyes. I'll soon be with you my love, To give you my dawn surprise. I'll be with you darling soon, I'll be with you when the stars start falling. I've been waiting so longTo be where I'm goingIn the sunshine of your love. I'm with you my love, The light's shining through on you. Yes,  I'm with you my love, It's the morning and just we two. I'll stay with you darling now, I'll stay with you till my seas are dried up.",
      "gradient_color_stop_1": "#456bc6",
      "gradient_color_stop_2": "#b4f677",
      "gradient_color_stop_3": "#1cc13a",
      "pub_date": "2019-01-23T09:43:23.636748Z"
   }
]
````


````
http://127.0.0.1:8000/api
Method: GET
Returns:[
   {  
      "id":193,
      "entry_title":"jimi hendrix sunshine of your love",
      "entry":"It's getting near dawn,When lights close their tired eyes. I'll soon be with you my love, To give you my dawn surprise. I'll be with you darling soon, I'll be with you when the stars start falling. I've been waiting so longTo be where I'm goingIn the sunshine of your love. I'm with you my love, The light's shining through on you. Yes,  I'm with you my love, It's the morning and just we two. I'll stay with you darling now, I'll stay with you till my seas are dried up.",
      "gradient_color_stop_1":"#456bc6",
      "gradient_color_stop_2":"#b4f677",
      "gradient_color_stop_3":"#1cc13a",
      "pub_date":"2019-01-23T09:08:17.007633Z"
   }
] 
````
