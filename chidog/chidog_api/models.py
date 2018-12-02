from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Pet(models.Model):
	first_name = models.CharField(max_length=100)
	middle_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	age = models.IntegerField(default=0)
	breed = models.CharField(max_length=100)
	owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pets', default=None)

	def __str__(self):
		return self.first_name + ' | ' + self.owner.username

class Post(models.Model):
	date_time = models.DateTimeField(default=timezone.now)
	modified = models.DateTimeField(default=timezone.now)
	post_body = models.TextField()
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', default=None)

	def __str__(self):
		return self.created_by.username + ' | ' + self.post_body

class Photo(models.Model):
	picture_url = models.CharField(max_length=255)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pictures', default=None)

	def __str__(self):
		return self.picture_url


class Reply(models.Model):
	date_time = models.DateTimeField(default=timezone.now)
	modified = models.DateTimeField(default=timezone.now)
	reply_body = models.TextField()
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='replies', default=None)
	replied_to = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='replies', default=None)

	def __str__(self):
		return self.created_by.username + ' | ' + self.reply_body