from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('external', 'External'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    # Custom fields
    reg_no = models.CharField(max_length=50, unique=True, null=True, blank=True)
    employee_id = models.CharField(max_length=50, unique=True, null=True, blank=True)

    phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.usernameclass Relation(models.Model):
    external_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='external_user')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_user')

    relation_type = models.CharField(max_length=20)  # parent / sibling
    status = models.CharField(max_length=20, default='pending')  # pending / approved