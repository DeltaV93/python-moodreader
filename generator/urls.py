from django.urls import path

from . import views
from . import api

app_name = 'generator'
urlpatterns = [
    path('', views.index, name='index'),
    # path('mood/new', views.new_mood, name='mood'),
    path('mood/past', views.past_moods, name='past_moods'),
    path('mood/<int:pk>/', views.detail_mood, name='detail_mood'),
    path('api', api.mood_generator),
    path('api/list', api.MoodView.as_view()),
]
