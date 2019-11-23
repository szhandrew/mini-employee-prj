from django.urls import path, include

from staff import views

urlpatterns = [
	path('register/', views.register)
]