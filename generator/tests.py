from django.test import TestCase, Client
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from .models import Dictionary, Entry


class EntryTest(APITestCase):
    def setUp(self):
        # self.client = Client()
        self.entry_title = 'Hey Jude'
        self.entry = 'Hey Jude, don\'t make it bad' + \
                     'Take a sad song and make it better' + \
                     'Remember to let her into your heart' + \
                     'Then you can start to make it better' + \
                     'Hey Jude, don\'t be afraid' + \
                     'You were made to go out and get her' + \
                     'The minute you let her under your skin' + \
                     'Then you begin to make it better' + \
                     'And anytime you feel the pain, hey Jude, refrai' + \
                     'Don\'t carry the world upon your shoulders' + \
                     'For well you know that it' + \
                     'By making his world a little colder' + \
                     'Nah nah nah nah nah nah nah nah ' + \
                     'Hey Jude, don\'t let me down' + \
                     'You have found her, now go and get her' + \
                     'Remember to let her into your heart' + \
                     'Then you can start to make it better'
        # TEST TO MAKE SURE THE POST REQUEST IS WORKING

    def test_mood_generator_POST_new_mood(self):
        """
        Ensure we can create a new mood object.
        """
        url = reverse('mood_generator')
        data = {
            'entry_title': self.entry_title,
            'entry': self.entry,
            'gradient_color_stop_1': '',
            'gradient_color_stop_2': '',
            'gradient_color_stop_3': '',
            'pub_date': '',
        }
        response = self.client.post(url, data, format='json')
        print(response.status_code)
        #  CHECK TO MAKE SURE THIS IS A GOOD RESPONSE
        self.assertEquals(response.status_code, 200)
        #   TODO | REFACTOR THE VIEW CODE SO I CAN TEST THAT COLORS CAN BE SENT COLOR LIST
