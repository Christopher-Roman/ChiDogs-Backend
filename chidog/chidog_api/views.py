from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Pet, Post, Photo, Reply
from django.contrib.auth.models import User
from django.http import JsonResponse
import json

# Create your views here.

# Pet Views and Routes for the pets that users can add to their profile.

class Pets(View):
	# Pet Get Route
	def get(self, request):
		if(request.user.is_authenticated):
			user = User.objects.get(id=request.user.id)
			pet_list = list(user.pets.all().values())
			response_data = pet_list,
			return JsonResponse({
				'Content-Type': 'application/json',
				'credentials': 'include',
				'status': 200,
				'data': pet_list,
				}, safe=False)

	# Pet Post Route
	def post(self, request):
		data = request.body.decode('utf-8')
		data = json.loads(data)
		try:
			new_pet = Pet(first_name=data['first_name'], middle_name=data['middle_name'], last_name=data['last_name'], age=data['age'], breed=data['breed'])
			new_pet.owner = request.user
			new_pet.save()
			data['id'] = new_pet.id
			return JsonResponse({'data': data}, safe=False)
		except:
			return JsonResponse({'error', 'Data not valid.'}, safe=False)

class Pet_Detail(View):

	# Pet Detail view Get Route
	def get(self, request, pk):
		pet_list = list(Pet.object.filter(pk=pk).values)
		return JsonResponse({'data': pet_list}, safe=False)

	# Pet Detail View Edit Route
	def put(self, request, pk):
		data = request.body.decode('utf-8')
		data = json.loads(data)
		try:
			edit_pet = Pet.objects.get(pk=pk)
			data_key = list(data.keys())

			for key in data_key:
				if key == 'first_name':
					edit_pet.first_name = data[key]
				if key == 'middle_name':
					edit_pet.middle_name = data[key]
				if key == 'last_name':
					edit_pet.last_name = data[key]
				if key == 'age':
					edit_pet.age = data[key]
				if key == 'breed':
					edit_pet.breed = data[key]
				edit_pet.save()
				data['id'] = edit_pet.id
				return JsonResponse({'data': data}, safe=False)
		except Pet.DoesNotExist:
			return JsonResponse({'error': 'Pet does not exist.'})
		except:
			return JsonResponse({'error': 'Something went wrong.'}, safe=False)

	# Pet Delete Route
	def delete(self, request, pk):
		try:
			pet_to_delete = Pet.objects.get(pk=pk)
			pet_to_delete.delete()
			return JsonResponse({'data': 'Removal was successful.'}, safe=False)
		except:
			return JsonResponse({'data': 'Removal failed. Please try again.'})

# These are the Views and Routes for the Posts that users can make. 

class Posts(View):

	# Posts Get Route
	def get(self, request):
		if(request.user.is_authenticated):
			user = User.object.get(id=request.user.id)
			post_list = list(user.post.all().values())
		return JsonResponse({
			'Content-Type': 'application/json',
			'credentials': 'include',
			'status': 200,
			'data': post_list
			}, safe=False)

		# Posts Post Route
		def post(self, request):
			data = request.body.decode('utf-8')
			data = json.loads(data)

			try:
				new_post = Post(post_body=data['post_body'])
				new_post.created_by = request.user
				new_post.save()
				data['id'] = new_post.id
				return JsonResponse({'data': data}, safe=False)
			except:
				return JsonResponse({'error': 'Data not valid'}, safe=False)

class Post_Detail(View):

	# Post Detail Get Route
	def get(self, request, pk):
		post_list = list(Post.object.filter(pk=pk).values)
		return JsonResponse({'data': post_list}, safe=False)

	# Posts Detail Edit Route
	def put(self, request, pk):
		data = request.body.decode('utf-8')
		data = json.loads(data)
		try:
			edit_post = Post.objects.get(pk=pk)
			data_key = list(data.keys())

			for key in data_key:
				if key == 'post_body':
					edit_post.post_body = data[key]
			edit_post.save()
			data['id'] = edit_post.id
			return JsonResponse({'data': data}, safe=False)
		except Post.DoesNotExist:
			return JsonResponse({'data': 'Post does not exist.'})
		except:
			return JsonResponse({'data': 'Something went wrong.'}, safe=False)

	# Post Delete Route
	def delete(self, request, pk):
		try:
			post_to_delete = Post.object.get(pk=pk)
			post_to_delete.delete()
			return JsonResponse({'data': 'Delete successful'})
		except:
			return JsonResponse({'data': 'Delete failed.'})


# These are the Views and Routes for Replies that users can create.

class Replies(View):

	# Reply Get Route
	def get(self, request):
		if(request.user.is_authenticated):
			user = User.objects.get(id=request.user.id)
			reply_list = list(user.replies.all().values())
		return JsonResponse({
			'Content-Type': 'application/json',
			'credentials': 'include',
			'status': 200,
			'data': reply_list
			}, safe=False)

	# Reply Post Route
	def post(self, request, pk):
		data = request.body.decode('utf-8')
		data = json.loads(data)

		try:
			new_reply = Reply(reply_body=data['reply_body'])
			new_reply.replied_to = req.params.pk
			new_reply.created_by = request.user
			data['id'] = new_reply
			return JsonResponse({'data': data}, safe=False)
		except:
			return JsonResponse({'error': 'Data not valid'}, safe=False)

class Reply_Detail(View):

	# Reply detail Get Route
	def get(self, request,pk):
		reply_list = list(Reply.object.filter(pk=pk).values)
		return JsonResponse({'data': reply_list}, safe=False)

	# Reply Edit Route
	def put(self, request, pk):
		data = request.body.decode('utf-8')
		data = json.loads(data)

		try:
			edit_reply = Reply.objects.get(pk=pk)
			data_key = list(data.keys())

			if key == 'reply_body':
				edit_reply.reply_body = data[key]
			edit_reply.save()
			data['id'] = edit_reply.id
			return JsonResponse({'data': data}, safe=False)
		except Reply.DoesNotExist:
			return JsonResponse({'error': 'Reply does not exist.'})
		except:
			return JsonResponse({'error': 'Something went wrong.'}, safe=False)

	#Reply Delete Route
	def delete(self, request, pk):
		try:
			reply_to_delete = Reply.objects.get(pk=pk)
			reply_to_delete.delete()
			return JsonResponse({'data': 'Delete successful.'})
		except:
			return JsonResponse({'data': 'Something went wrong.'})

