from django.urls import path

from . import views

app_name = 'generator'
urlpatterns = [
    path('', views.index, name='index'),
    path('mood/', views.generate_mood, name='mood'),
    path('mood/past', views.past_moods, name='past_moods'),
    path('<int:entry_id>/mood/', views.generate_mood, name='mood')
]
