from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('lead', 'Project Lead'),
        ('developer', 'Developer'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()
    completed = models.BooleanField(default=False)
    lead = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='led_projects')

class Document(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Assignment(models.Model):
    developer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'developer'})
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
