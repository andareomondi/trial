from django.shortcuts import redirect, render
from django.views import View
from member.models import Member
from django.contrib import messages
# Create your views here.
class Dashboard(View):
    def get(self, request):
        if request.user.is_superuser:
            members = Member.objects.all()
            memberscount = members.count()
            context = {
                'members': members,
                'memberscount': memberscount,
            }
            return render(request, 'managment/dashboard.html', context=context)
        else:
            return redirect(to='login')
    def post(self, request):
        member_id = request.POST.get('id')
        member = Member.objects.get(id=member_id)
        member.delete()
        messages.success(request,  'Member deleted successfully')
        members = Member.objects.all()
        memberscount = members.count()
        context = {
            'members': members,
            'memberscount': memberscount,
        }
        return render(request,  'managment/dashboard.html', context=context)
