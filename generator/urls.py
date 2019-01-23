from django.urls import path

from . import views

app_name = 'generator'
urlpatterns = [
    path('', views.index, name='index'),
    path('mood/past', views.past_moods, name='past_moods'),
    path('mood/<int:pk>/', views.detail_mood, name='detail_mood'),
    path('api', views.mood_generator),
    path('api/list', views.mood_generator),
]
