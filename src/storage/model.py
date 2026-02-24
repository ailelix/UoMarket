from django.contrib.auth.models import AbstractUser
from django.db import models


class StudentUserModel(AbstractUser):
    """A student user model inherited from Django.AbstractUser"""
    fullname = models.CharField(max_length=100, blank=True, verbose_name="Full name")
    student_id = models.CharField(max_length=8, blank=True, verbose_name="Student ID")

    def __str__(self):
        return f"{self.fullname} - {self.student_id}"
