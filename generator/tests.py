from django.test import TestCase
from django.test.client import Client
from django.utils import timezone


class TestEntryView(TestCase):
    def setUp(self):
        self.client = Client()
        self.entry_title = 'Jimi hendrix sunshine of your love'
        self.entry = "It's getting near dawn,When lights close their tired eyes.I'll soon be with you my love," \
                     "To give you my dawn surprise.I'll be with you darling soon,I'll be with you when the stars " \
                     "start falling.I've been waiting so longTo be where I'm goingIn the sunshine of your love.I'm " \
                     "with you my love,The light's shining through on you.Yes, I'm with you my love,It's the morning " \
                     "and just we two.I'll stay with you darling now,I'll stay with you till my seas are dried up."
        self.color_1 = ' 1'
        self.color_2 = '2 '
        self.color_3 = ' 3'
        self.pub_date = timezone.now()

    # TEST TO MAKE SURE THE POST REQUEST IS WORKING

    def test_mood_generator_POST_new_mood(self):
        response = self.client.post('/api', {
            'entry_title': self.entry_title,
            'entry': self.entry,
            'gradient_color_stop_1': self.color_1,
            'gradient_color_stop_2': self.color_1,
            'gradient_color_stop_3': self.color_1,
            'pub_date': self.pub_date,
        })
        #  CHECK TO MAKE SURE ENTRY WAS CREATED RESPONSE
        self.assertEquals(response.status_code, 201)
        # TODO / FIND OUT WHY PYCHARM TEST DIFFER FROM TERMINAL
        # self.assertEquals(response.data['gradient_color_stop_3'], '#1cc13a')

    def test_mood_generator_GET_all_mood(self):
        response = self.client.get('/api')
        self.assertEquals(response.status_code, 200)
