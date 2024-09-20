from django.urls import path
from . import views

urlpatterns = [
	path('logout/', views.sign_out, name='logout'),
]