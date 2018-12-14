from django.views import View
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from chidog_api.models import Pet, Post, Photo, Reply
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib import auth
import json

# Create your models here.

@ensure_csrf_cookie
def getToken(request):
	return JsonResponse({'data': 'Token received'}, safe=False)

def logout(request):
	auth.logout(request)
	return JsonResponse({'data': 'Logout Successful'})


class Create_User(View):

	def post(self, request):
		data = request.body.decode('utf-8')
		data = json.loads(data)
		try:
			new_user = User(username=data['username'], email=data['email'], password=data['password'])
			new_user.set_password(new_user.password)
			new_user.save()
			auth.login(request, new_user)
			return JsonResponse({'data': 'Registration Successful'}, safe=False)
		except: 
			return JsonResponse({'data': 'Registration Failed.'}, safe=False)

class Authentication(View):
	
	def post(self, request):
		data = request.body.decode('utf-8')
		data = json.loads(data)
		user = auth.authenticate(username=data['username'], password=data['password'])
		if user is not None:
			auth.login(request, user)
			print(request)
			return JsonResponse({'data': 'Login Successful'}, safe=False)
		else:
			return JsonResponse({'data': 'Login failed. Try again.'}, safe=False)

class User_Detail(View):
	def get(self, request):
		if(request.user.is_authenticated):
			usersPets = list(Pet.objects.all().values())
			return JsonResponse({
					'Content-Type': 'application/json',
					'credentials': 'include',
					'status': 200,
					'data': usersPets,
					}, safe=False)

class Post_Detail(View):
	def get(self, request):
		if(request.user.is_authenticated):
			posts = list(Post.objects.all().values())
			return JsonResponse({
				'Content-Type': 'application/json',
				'credentials': 'include',
				'status': 200,
				'data': posts,
				}, safe=False)
		else:
			return JsonResponse({
				'Content-Type': 'application/json',
				'credentials': 'include',
				'status': 200,
				'message': 'Must be logged in.',
				}, safe=False)


