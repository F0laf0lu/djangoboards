from django.urls import path
from . import views


urlpatterns = [
    path('', views.BoardListView.as_view(), name='home'),
    # path('board/<int:pk>', views.board_topics, name='board_topics'),
    path('board/<int:pk>', views.TopicListView.as_view(), name='board_topics'),
    path('board/<int:pk>/new_topic', views.new_topic, name='new_topic'),
    # path('board/<int:pk>/<int:topic_pk>', views.topic_post, name='topic_post'),
    path('board/<int:pk>/<int:topic_pk>', views.PostListView.as_view(), name='topic_post'),
    path('board/<int:pk>/<int:topic_pk>/reply', views.reply_topic, name='reply_topic'),
    path('board/<int:pk>/<int:topic_pk>/<int:post_pk>/edit', views.PostUpdateView.as_view(), name='edit_post'),
]
