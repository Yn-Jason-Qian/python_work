from django.urls import path
from django.conf.urls import url
from . import views

app_name = 's_blogs'
urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    url(r'^topic/(?P<topic_id>\d+)$', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    url(r'^topic/(?P<topic_id>\d+)/new_entry/', views.new_entry, name='new_entry')
]