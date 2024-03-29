from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    birth = models.DateField(blank =True,null=True)
    phone = models.CharField(max_length=20,null=True)

    def __str_(self):
        return f'user {self.user.username}'

