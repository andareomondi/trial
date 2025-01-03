from django.shortcuts import render, redirect
from django.views import View
from member.models import *
# Create your views here.
class Dashboard(View):
    def get(self, request,):
      if (request.user.is_authenticated & request.user.is_superuser):

        members = Member.objects.all()
        context = {
          'members': members,
        }
        return render(request, 'managment/dashboard.html', context=context)
      else:
         return redirect(to='home')

class SermonCreation(View):
    def get(self, request):
      return render(request, 'managment/sermon_form.html')

    def post(self, request):
      pass