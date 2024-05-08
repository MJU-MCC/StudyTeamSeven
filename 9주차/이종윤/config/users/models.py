from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    profile_image=models.ImageField(
        "프로필 이미지",upload_to="user/profile", blank=True)
    short_description=models.TextField("소개글", blank=True)
    
# Create your models here.
