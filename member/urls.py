from django.urls import path
from . import views

urlpatterns = [
	path('logout/', views.sign_out, name='logout'),
	path('login/', views.login, name='login'),
	path('contactform/', views.contactform, name='contactform'),
]