from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.

# authentication views
class Register(View):
    def post(self, request):
        first_name = request.POST.get('first_name')
        second_name = request.POST.get('second_name')
        email = request.POST.get('signupEmail')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('signupPassword')
        residence = request.POST.get('residence')
        profile_pic = request.POST.get('profile_pic')
        print(first_name, second_name, phone_number, email, password, profile_pic)
        try:
            user = Member.objects.create_user(first_name=first_name, second_name=second_name, email=email, phone_number=phone_number, password=password)
            user.save()
            messages.success(request, 'Account creation succesful. Proceed to Login')
            return redirect(to='login')
        except:
            messages.error(request, 'Email already in the system')
            return render(request, 'member/authentication.html')



class Login(View):
     def get(self, request):
         if request.user.is_authenticated:
             return redirect(to='home')
         else:
             return render(request, 'member/authentication.html')
     def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        member = Member.objects.filter(email=email).first()
        if member is None:
            messages.error(request, message="Email not found in the system")
            return render(request, "member/authentication.html")
        else:
            member = authenticate(email=email, password=password)
            if member is not None:
                login(request, member)
                messages.success(request, 'Login successful')
                return redirect(to="home")
            else:
                messages.error(request, message="Incorrect password")
                return render(request, "member/authentication.html")

class SignOut(View):
    def get(self, request):
        logout(request)
        messages.success( request, 'Goodbye')
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
        def post(self, request, pk):
            user = Member.objects.get(id=pk)
            address = request.POST.get('address')
            print(address)
            print(request.POST.get('address'))
            user.address = request.POST.get('address')
            user.save()
            messages.success(request, 'Update succesful')
            return render(request, 'member/profile.html')



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
