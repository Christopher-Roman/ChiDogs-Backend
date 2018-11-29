from django.urls import path
from .views import Pets

urlpatterns = [
	path('', Pets.as_view())
]