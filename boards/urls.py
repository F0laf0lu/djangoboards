from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('board/<int:pk>', views.board_topics, name='board_topics'),
    path('board/<int:pk>/new_topic', views.new_topic, name='new_topic')
]
