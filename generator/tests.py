from time import sleep

from django.test import TestCase
from django.test.client import Client
from django.utils import timezone

c = Client()
message_interval = 1 # seconds
not_long_enough = 0.7 # seconds
long_enough = 1.3 # seconds

class TestEntryView(TestCase):
    def setUp(self):
        self.client = Client()
        self.entry_title = 'jimi hendrix sunshine of your love'
        self.entry = "It's getting near dawn,When lights close their tired eyes.I'll soon be with you my love,To give you my dawn surprise.I'll be with you darling soon,I'll be with you when the stars start falling.I've been waiting so longTo be where I'm goingIn the sunshine of your love.I'm with you my love,The light's shining through on you.Yes, I'm with you my love,It's the morning and just we two.I'll stay with you darling now,I'll stay with you till my seas are dried up."
        self.color_1 = ' 1'
        self.color_2 = '2 '
        self.color_3 = ' 3'
        self.pub_date = timezone.now()

    # TEST TO MAKE SURE THE POST REQUEST IS WORKING

    def test_mood_generator_POST_new_mood(self):
        response = c.post('/api', {
            'entry_title': 'jimi hendrix sunshine of your love',
            'entry': "It's getting near dawn,When lights close their tired eyes. I'll soon be with you my love, To give you my dawn surprise. I'll be with you darling soon, I'll be with you when the stars start falling. I've been waiting so longTo be where I'm goingIn the sunshine of your love. I'm with you my love, The light's shining through on you. Yes,  I'm with you my love, It's the morning and just we two. I'll stay with you darling now, I'll stay with you till my seas are dried up. ",
            'gradient_color_stop_1': '1',
            'gradient_color_stop_2': '1',
            'gradient_color_stop_3': '1',
            'pub_date': timezone.now(),
        })
        #  CHECK TO MAKE SURE ENTRY WAS CREATED RESPONSE
        sleep(2.3)
        self.assertEquals(response.status_code, 201)
        # TODO / FIND OUT WHY PYCHARM TEST DIFFER FROM TERMINAL
        # self.assertEquals(response.data['gradient_color_stop_3'], '#7304e9')

    def test_mood_generator_GET_all_mood(self):
        response = c.get('/api')
        self.assertEquals(response.status_code, 200)



