from django.urls import path
from .views import Create_User, Authentication, User_Detail, logout, getToken

urlpatterns = [
	path('', Create_User.as_view()),
	path('login/', Authentication.as_view()),
	path('<int:pk>/', User_Detail.as_view()),
	path('logout/', logout),
	path('getToken', getToken)
]