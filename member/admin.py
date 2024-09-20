from django.contrib import admin
from .models import Member, ChurchImage, Choir, ChoirImage, ChoirPracticeDay, Sermon, Point, CedGroup, CedPracticeDay 

# Register your models here.
admin.site.register(Member)
admin.site.register(ChurchImage)
admin.site.register(Choir)
admin.site.register(ChoirImage)
admin.site.register(ChoirPracticeDay)
admin.site.register(Sermon)
admin.site.register(Point)
admin.site.register(CedGroup)
admin.site.register(CedPracticeDay)
