from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Project, Document

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'role')

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'deadline', 'completed']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['project', 'file']
