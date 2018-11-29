from django.views import View
from .models import Pet, Post, Photo, Reply
from django.contrib.auth.models import User
from django.http import JsonResponse
import json

# Create your views here.

class Pets(View):
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

	def post(self, request):
		data = request.body.decode('utf-8')
		data = json.loads(data)
		try:
			new_pet = Pet(first_name=data['first_name'], middle_name=data['middle_name'], last_name=data[last_name], age=data['age'], breed=data['breed'])
			new_pet.owner = request.user
			new_pet.save()
			data['id'] = new_pet.id
			return JsonResponse({'data': data}, safe=False)
		except:
			return JsonResponse({'error', 'Data not valid.'}, safe=False)

class Pet_Detail(View):
	def get(self, request, pk):
		pet_list = list(Pet.object.filter(pk=pk).values)
		return JsonResponse({'data': pet_list}, safe=False)

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

	def delete(self, request, pk):
		try:
			pet_to_delete = Pet.object.get(pk=pk)
			pet_to_delete.delete()
			return JsonResponse({'data': 'Removal was successful.'}, safe=False)
		except:
			return JsonResponse({'data': 'Removal failed. Please try again.'})

# class Posts(View):
# 	def get(self, request):
		





