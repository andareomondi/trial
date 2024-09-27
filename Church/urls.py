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
    path('about/', About.as_view(), name='about'),
    path('history/', History.as_view(), name='history'),
    path('login/', Login.as_view(), name='login'),
    path('accounts/', include('member.urls')),
    path('register/', Register.as_view(), name='register'),
    path('profile/<int:pk>/', Profile.as_view(), name='profile'),
    path('gallery/', ChurchGallery.as_view(), name='churchgallery'),
    path('choirs/', Choirs.as_view(), name='choirs'),
    path('specific-choir/<int:pk>/', SpecificChoir.as_view(), name='specific-choir'),
    path('sunday-school/', SundaySchool.as_view(), name='sunday-school'),
    path('word/', Word.as_view(), name='word'),
    path('details/<int:pk>/', SermonPoints.as_view(), name='details'),
    path('cedgroups/', CedGroups.as_view(), name='cedgroups'),
    path('specific-cedgroup/<int:pk>/', SpecificCedGroup.as_view(), name='specific-cedgroup'),    
    path('prayer-cells/', PrayerCells.as_view(), name='prayer-cells'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('create_sermon/', CreateSermon.as_view(), name='create_sermon'),
    path('churchleaders', ChurchLeaders.as_view(), name='churchleaders')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
