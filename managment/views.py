from django.shortcuts import render, redirect
from django.views import View
from member.models import *
from django.contrib import messages
# Create your views here.
class Dashboard(View):
    def get(self, request):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                inquiries = ContactForm.objects.all()
                members = Member.objects.all()
                memberscount = members.count()
                context = {
                    'members': members,
                    'memberscount': memberscount,
                    'inquiries': inquiries,
                }
                return render(request,  'managment/dashboard.html', context=context)
            else:
                return redirect('home')
        else:
            return redirect('login')
    def post(self, request):
        member_id = request.POST.get('id')
        member = Member.objects.get(id=member_id)
        # print(member_id)
        member.delete()
        messages.success(request,  'Member deleted successfully')
        members = Member.objects.all()
        memberscount = members.count()
        context = {
            'members': members,
            'memberscount': memberscount,
        }
        return render(request,  'managment/dashboard.html', context=context)

class SermonCreation(View):
    def get(self, request):
      return render(request, 'managment/sermon_form.html')

    def post(self, request):
      pass