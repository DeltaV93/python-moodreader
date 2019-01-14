from django.test import TestCase, Client
from django.urls import reverse


class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.entry_url = reverse('generator:index')
        self.mood_url = reverse('generator:mood')
        self.entry = 'Hey Jude, don\'t make it bad ' \
                     'Take a sad song and make it better ' \
                     'Remember to let her into your heart ' \
                     'Then you can start to make it better'
    # TEST TO MAKE SURE THE POST REQUEST IS WORKING

    def test_mood_generator_POST_new_mood(self):
        response = self.client.post(self.entry_url, {'mood-entry': self.entry}, content_type="application/json")
        print(response.status_code)
        #  CHECK TO MAKE SURE THIS IS A GOOD RESPONSE
        self.assertEquals(response.status_code, 200)
        #   TODO | REFACTOR THE VIEW CODE SO I CAN TEST THAT COLORS CAN BE SENT COLOR LIST
