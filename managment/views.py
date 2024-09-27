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
        from twilio.rest import Client
        book=request.POST['book']
        verse=request.POST['verse']
        description = request.POST['description']
        members = Member.objects.all()
        for member in members:
            print(member.phone_number)
            try:
                account_sid = 'AC565bc45825da07a5157ba5ef0f867928'
                auth_token = '1def00172e44b6b0deb3e23217cebc30'
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                from_='whatsapp:+14155238886',
                body=f'The message for today comes from the book of  {book} verse {verse}.\n--------Description------\n{description}',
                to=f'whatsapp:+254{member.phone_number}'
                )

            except:
                pass
        messages.success(request, message='The sermon has been sent successfully')
        return render(request,  template_name='managment/create_sermon.html')

