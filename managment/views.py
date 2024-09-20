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
        sermon = Sermon(
            image=request.FILES['image'],
            book=request.POST['book'],
            verse=request.POST['verse'],
            description=request.POST['description']
        )
        sermon.save()

        # Get the list of point fields from the request.POST dictionary
        point_fields = [key for key in request.POST.keys() if key.startswith('point_')]
        description_fields = [key for key in request.POST.keys() if key.startswith('description_')]

        # Create multiple Point instances associated with the sermon
        for i, point_field in enumerate(point_fields):
            point = Point(
                word=sermon,
                point=request.POST[point_field],
            )
            point.save()
        messages.success(request, message='The sermon has been added successfully')
        return render(request,  template_name='managment/create_sermon.html')

