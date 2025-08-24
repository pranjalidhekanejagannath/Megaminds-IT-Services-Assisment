from django.contrib import admin
from .models import CustomUser, Project, Document, Assignment
from django.contrib.auth.admin import UserAdmin
# Register your models here.


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Project)
admin.site.register(Document)
admin.site.register(Assignment)
