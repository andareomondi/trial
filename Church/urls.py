"""
URL configuration for Church project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from member.views import *
from managment.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path("about/", About.as_view(), name="about"),
    path("sermons/", Word.as_view(), name="sermon"),
    path("specific-sermon/<int:pk>/", SpecificSermon.as_view(), name="specific-sermon"),
    path("prayers/", PrayerCells.as_view(), name="prayers"),
    path("login/", Login.as_view(), name="login"),
    path("profile/<int:pk>/", Profile.as_view(), name="Profile"),
    path("register/", Register.as_view(), name="Register"),
    path("signOut/", SignOut.as_view(), name="SignOut"),
    path("dashboard/", Dashboard.as_view(), name="dashboard"),
    path("sermon-creation/", SermonCreation.as_view(), name="sermon_creation"),
    path("gallery/", Gallery.as_view(), name="gallery"),
    path("sundayschool/", SundaySchool.as_view(), name="sundayschool"),
    path("cedgroups/", CEDGroups.as_view(), name="cedgroups"),
    path("specific-ced-group/<int:pk>/", SpecificCedGroup.as_view(), name="specific-ced-group"),
    path("choirs/", Choirs.as_view(), name="choirs"),
    path("specific-choir/<int:pk>/", SpecificChoir.as_view(), name="specific-choir"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
