from django.shortcuts import redirect, render
from django.views import View
from member.models import Member, Sermon, Point
from django.contrib import messages
# Create your views here.
class Dashboard(View):
    def get(self, request):
        if request.user.is_superuser:
            members = Member.objects.all()
            context = {
                'members': members
            }
            return render(request, 'managment/dashboard.html', context=context)
        else:
            return redirect(to='login')
class CreateSermon(View):
    def get(self, request):
        return render(request, template_name='managment/create_sermon.html')

    def post(self, request):
        book=request.POST['book']
        verse=request.POST['verse']
        description = request.POST['description']
        members = Member.objects.all()
        messages.success(request, message='The sermon has been sent successfully')
        return render(request,  template_name='managment/create_sermon.html')

