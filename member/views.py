from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
# Create your views here.

# authentication views
class Login(View):
     def get(self, request):
         if request.user.is_authenticated:
             return redirect(to='home')
         else:
             print(request.path)
             return render(request, 'member/authentication.html')
     def post(self, request):
        user = Member()
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=username, password=password)
        if user is not None:
            login(request, user)
            data = {
                'redirect':'/',
                'status': 'success',
                'message': 'Login successful',
            }
            return JsonResponse(data)
        else:
            data = {
                'status': 'error',
                'message': 'Invalid login credentials'
            }
            return JsonResponse(data)

class Register(View):
     def post(self, request):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password != password2:
            data = {
                'status': 'error',
                'message': 'Passwords do not match'
            }
            return JsonResponse(data)
        else:
            user = Member.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name, phone_number=phone_number)
            user.save()
            data = {
                'redirect': '/',
                'status': 'success',
                'message': 'User registered successfully'
            }
            return JsonResponse(data)

class SignOut(View):
    def get(self, request):
        logout(request)
        return redirect(to='home')

# Important views handled here for the app
class Home(View):
    def get(self, request):
        return render(request, 'member/home.html')

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name='member/about.html')

# specific views for specific sections
class Word(View):
	def get(self, request):
          if request.user.is_authenticated:
            words = Sermon.objects.all()
            context = {
                'words': words,
            }
            return render(request, 'member/sermons.html', context=context)
          else:
              return redirect(to='home')

class SpecificSermon(View):
    def get(self, request, pk):
        word = Sermon.objects.get(id=pk)
        points = word.point_set.all()
        context = {
            'word': word,
            'points': points
        }
        return render(request, 'member/specific-sermon.html', context = context)

class PrayerCells(View):
     def get(self, request):
          if request.user.is_authenticated:
            return render(request, 'member/prayercells.html')
          else:
              return redirect(to='home')
class Profile(View):
        def get(self, request, pk):
            if request.user.is_authenticated:
                user = Member.objects.get(id=pk)
                context = {
                    'user': user,
                }
                return render(request, 'member/profile.html', context=context)
            else:
                return redirect(to='login')
class Gallery(View):
    def get(self, request):
        if request.user.is_authenticated:
            images = ChurchImage.objects.all()
            videos = Video.objects.all()
            context = {
                'images':images,
                'videos':videos,
            }
            return render(request, template_name='member/gallery.html', context=context)
        else:
            return redirect('home')

class SundaySchool(View):
     def get(self, request):
          if request.user.is_authenticated:
            return render(request, 'member/sundayschool.html')
          else:
              return redirect('home')

class CEDGroups(View):
     def get(self, request):
          if request.user.is_authenticated:
            groups = CedGroup.objects.all()
            for group in groups:
                print('haga' if group != '' else 'kichwa hii')
            context = {
                'groups': groups
            }
            return render(request, 'member/cedgroups.html', context = context)
          else:
              return redirect('home')
class SpecificCedGroup(View):
     def get(self, request, pk):
        if request.user.is_authenticated:
            group = CedGroup.objects.get(id=pk)
            practice = group.cedpracticeday_set.all()
            context = {
                'cedgroup': group,
                'practice': practice,
            }
            return render(request, 'member/cedgroup.html', context=context)
        else:
            return redirect('home')

class Choirs(View):
     def get(self, request):
          if request.user.is_authenticated:
            choirs  = Choir.objects.all()
            context = {
                'choirs': choirs
            }
            return render(request, 'member/choirs.html', context = context)
          else:
              return redirect('home')
class SpecificChoir(View):
     def get(self, request, pk):
        if request.user.is_authenticated:
            choir = Choir.objects.get(id=pk)
            practice = choir.choirpracticeday_set.all()
            images = choir.choirimage_set.all()
            context = {
                'choir': choir,
                'images': images,
                'practice': practice,
            }
            return render(request, 'member/specific_choir.html', context=context)
        else:
            return redirect('home')
