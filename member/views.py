from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Member, ChurchImage, Choir, ChoirImage, Sermon, CedGroup, CedPracticeDay
# Create your views here.
class Home(View):
	def get(self, request):
		return render(request, 'member/index.html')

class About(View):
	def get(self, request):
		return render(request, 'member/about.html')
	def post(self, request):
		name = request.POST.get('name')
		messages.success(request, message=f'Hi {name}, your issue has been recieved and it is being worked upon')
		return render(request, 'member/about.html')		
class History(View):
	def get(self, request):
		return render(request, 'member/history.html')
class Login(View):
	def get(self, request):
		if request.user.is_authenticated:
			return redirect(to='home')
		else:
			return render(request=request, template_name='member/login.html')
	def post(self, request):
		email = request.POST.get('email')
		password = request.POST.get('password')
		member = authenticate(email=email, password=password)
		if member is not None:
			login(request, member)
			return redirect(to="home")
		else:
			messages.error(request, message="Wrong details provided")
			return render(request, "Member/login.html")

def sign_out(request):
	logout(request)
	return redirect(to='home')
class Register(View):
	def get(self, request):
		if request.user.is_authenticated:
			return redirect(to='home')
		else:
			return render(request, 'member/register.html')
	def post(self, request):
	    first_name = request.POST.get('first_name')
	    second_name = request.POST.get('second_name')
	    email = request.POST.get('email')
	    phone_number = request.POST.get('phone_number')
	    password = request.POST.get('password')
	    password2 = request.POST.get('password2')
	    if password != password2:
	        messages.error(request, message='The passwords should be matching')
	        return render(request, template_name='Member/register.html')
	    else:
	    	try:
	    		user = Member.objects.create_user(first_name=first_name, second_name=second_name, email=email, phone_number=phone_number, password=password)
	    		user.save()
	    		return redirect(to='login')
	    	except:
	    		messages.error(request, message='Email already in the system')
	    		return render(request, template_name='member/register.html')

class Profile(View):
	def get(self, request, pk):
		if request.user.is_authenticated:
			user = Member.objects.get(id=pk)
			context = {
				'user': user,
			}
			return render(request, template_name='member/profile.html', context=context)
		else:
			return redirect(to='login')
class ChurchGallery(View):
	def get(self, request):
		if request.user.is_authenticated:
			images = ChurchImage.objects.all()
			context = {
				'images': images,
			}
			return render(request, 'member/churchpictures.html', context=context)
		else:
			return redirect(to='login')
class Choirs(View):
	def get(self, request):
		if request.user.is_authenticated:
			choirs = Choir.objects.all()
			context = {
				'choirs': choirs,
			}
			return render(request, 'member/choirs.html', context=context)
		else:
			return redirect(to='login')

class SpecificChoir(View):
	def get(self, request, pk):
		if request.user.is_authenticated:
			choir = Choir.objects.get(id=pk)
			images = choir.choirimage_set.all()
			practice = choir.choirpracticeday_set.all()
			context = {
				'choir': choir,
				'images': images,
				'practice': practice,
			}
			return render(request, 'member/choirmedia.html', context=context)
		else:
			return redirect(to='login')
class SundaySchool(View):
	def get(self, request):
		if request.user.is_authenticated:
			return render(request, 'member/sundayschool.html')
class Word(View):
	def get(self, request):
		words = Sermon.objects.all()
		context = {
			'words': words,
		}
		return render(request, 'member/semorns.html', context=context)
class SermonPoints(View):
	def get(self, request, pk):
		word = Sermon.objects.get(id=pk)
		points = word.point_set.all()
		context = {
			'word': word,
			'points': points,
		}
		return render(request, 'member/more.html', context=context)

class CedGroups(View):
	def get(self, request):
		if request.user.is_authenticated:
			cedgroups = CedGroup.objects.all()
			context = {
				'cedgroups': cedgroups,
			}
			return render(request, 'member/cedgroups.html', context=context)
		else:
			return redirect(to='login')

class SpecificCedGroup(View):
	def get(self, request, pk):
		if request.user.is_authenticated:
			cedgroup = CedGroup.objects.get(id=pk)
			practice = cedgroup.cedpracticeday_set.all()
			context = {
				'cedgroup': cedgroup,
				'practice': practice,
			}
			return render(request, 'member/cedgroup.html', context=context)
		else:
			return redirect(to='login')
class PrayerCells(View):
	def get(self, request):
		if request.user.is_authenticated:
			return render(request, 'member/prayercells.html')
		else:
			return redirect(to='login')
	def post(self, request):
		name = request.POST.get('name')
		messages.success(request, message=f'Hi {name}, your issue has been recieved and it is being worked upon')
		return render(request, 'member/prayercells.html')
