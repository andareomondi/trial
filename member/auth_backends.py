# myapp/auth_backends.py
from django.contrib.auth.backends import BaseBackend
from .models import Member

class AuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        # Your custom authentication logic here
        try:
            member = Member.objects.get(email=email)
            if member.check_password(password):
                return member
        except Member.DoesNotExist:
            return None
    def get_user(self, user_id):
        try:
            return Member.objects.get(pk=user_id)
        except Member.DoesNotExist:
            return None
