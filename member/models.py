from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.
class MemberUserManager(BaseUserManager):
    def create_user(self, first_name, second_name, email, phone_number, password=None):
        if not email:
            raise ValueError('User should have an email')
        if not phone_number:
            raise ValueError('User should have an phone_number')        
        user = self.model(
            first_name=first_name,
            second_name=second_name,
            email = email,
            phone_number=phone_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, first_name, second_name, email, phone_number, password=None):
        user = self.create_user(
            first_name=first_name,
            second_name=second_name,
            email=email,
            phone_number=phone_number,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
           
class Member(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=255)
    phone_number = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_login = models.DateField(auto_now=True)
    profile_pic = models.ImageField(blank=True, upload_to='personal_profile_images', null=True)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = MemberUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'second_name', 'phone_number']

    def __str__(self):
        return f'{self.first_name} {self.second_name}'

class ChurchImage(models.Model):
    image = models.ImageField(upload_to='church-images')
class Choir(models.Model):
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=255)
    long_description = models.TextField(max_length=5000)
    leader = models.CharField(max_length=100)
    leader_number = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to='choir-profile-pics')

    def __str__(self):
        return self.name

class ChoirImage(models.Model):
    choir_name = models.ForeignKey(Choir, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='choir-images')

class ChoirPracticeDay(models.Model):
    DAYS_OF_THE_WEEK = (
        (1, 'Sunday'),
        (2, 'Monday'),
        (3, 'Tuesday'),
        (4, 'Wen'),
        (5, 'Thursday'),
        (6, 'Friday'),
        (7, 'Saturday'),
    )
    group = models.ForeignKey(Choir, on_delete=models.CASCADE)
    day = models.IntegerField(choices=DAYS_OF_THE_WEEK, null=True, blank=True)
    start = models.TimeField()
    stop = models.TimeField()

class Sermon(models.Model):
    image = models.ImageField(upload_to='sermon')
    book = models.CharField(max_length=255)
    verse = models.CharField(max_length=500)
    description = models.TextField(max_length=5000)
    preacher = models.CharField(max_length=255, default='Justus Mutuku')
    preacher_number = models.CharField(max_length=30, default='0717740400')
    preacher_profile_pic = models.ImageField(upload_to='preacher-profile-pics', default='static/assets/user.png')

    def __str__(self):
        return self.book
class Point(models.Model):
    word = models.ForeignKey(Sermon, on_delete=models.CASCADE)
    point = models.CharField(max_length=255)
    def __str__(self):
        return self.point
class CedGroup(models.Model):
    profile_pic = models.ImageField(upload_to='ced_profile_pics')
    name = models.CharField(max_length=255)
    founding = models.DateField()
    leader = models.CharField(max_length=100)
    leader_number = models.CharField(max_length=30)
    leader_profile_pic = models.ImageField(default='static/assets/user-default.png', upload_to='leader-profile')    
    short_description = models.CharField(max_length=255)
    long_description = models.TextField(max_length=5000)
    verse = models.CharField(max_length=255)
    mission = models.CharField(max_length=255)
    vision = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class CedPracticeDay(models.Model):
    DAYS_OF_THE_WEEK = (
        (1, 'Sunday'),
        (2, 'Monday'),
        (3, 'Tuesday'),
        (4, 'Wen'),
        (5, 'Thursday'),
        (6, 'Friday'),
        (7, 'Saturday'),
    )
    group = models.ForeignKey(CedGroup, on_delete=models.CASCADE)
    day = models.IntegerField(choices=DAYS_OF_THE_WEEK, null=True, blank=True)
    start = models.TimeField()
    stop = models.TimeField()

class Video(models.Model):
    video = models.FileField(upload_to='videos')
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title