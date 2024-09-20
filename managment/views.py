from django.shortcuts import redirect, render
from django.views import View
from member.models import Member
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
