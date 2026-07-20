from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ADMIN = 'admin'
    APPLICANT ='applicant'

    ROLE_CHOICES =[
        (ADMIN,'admin'),
        (APPLICANT,'applicant'),
    ]
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=APPLICANT,
    )

    def __str__(self):
        return self.username