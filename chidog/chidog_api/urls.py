from django.urls import path
from .views import Pets, Pet_Detail, Posts, Post_Detail, Replies, Reply_Detail

urlpatterns = [
	path('pets/', Pets.as_view()),
	path('posts/', Posts.as_view()),
	path('reply/', Replies.as_view()),
	path('pets/<int:pk>', Pet_Detail.as_view()),
	path('posts/<int:pk>', Post_Detail.as_view()),
	path('reply/<int:pk>', Reply_Detail.as_view())
]