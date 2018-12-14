from django.urls import path
from .views import Create_User, Authentication, User_Detail, logout, getToken, Post_Detail

urlpatterns = [
	path('', Create_User.as_view()),
	path('login/', Authentication.as_view()),
	path('user/', User_Detail.as_view()),
	path('post/', Post_Detail.as_view()),
	path('search/', User_Detail.as_view()),
	path('logout/', logout),
	path('getToken', getToken)
]