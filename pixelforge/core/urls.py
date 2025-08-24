# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.dashboard, name='dashboard'),  # this is the homepage
#     path('login/', views.login_view, name='login'),
#     path('logout/', views.logout_view, name='logout'),
#     path('register/', views.register, name='register'),
#     path('upload/', views.upload_document, name='upload'),
#     path('project/<int:project_id>/assign/', views.assign_developers, name='assign'),
#     path('project/<int:project_id>/documents/', views.view_documents, name='documents'),
# ]

# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_redirect, name='home'),  # Redirect root to dashboard
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('assign/<int:project_id>/', views.assign_developers, name='assign_developers'),
    path('upload/', views.upload_document, name='upload_document'),
    path('documents/<int:project_id>/', views.view_documents, name='view_documents'),
]
