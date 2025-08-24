from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, DocumentForm
from .models import Project, Assignment, Document, CustomUser
from django.contrib import messages
from django.shortcuts import redirect

def home_redirect(request):
    return redirect('dashboard')
# ========================
# Authentication Views
# ========================
def register(request):
    if request.user.role != 'admin':
        return redirect('login')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User registered successfully.")
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()

    return render(request, 'core/register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'login.html')  # <-- Make sure this file exists in templates/


def logout_view(request):
    logout(request)
    return redirect('login')


# ========================
# Dashboard + Projects
# ========================

@login_required
def dashboard(request):
    user = request.user
    if user.role == 'admin':
        projects = Project.objects.all()
    elif user.role == 'lead':
        projects = Project.objects.filter(lead=user)
    else:  # developer
        projects = Project.objects.filter(assignment__developer=user)

    return render(request, 'dashboard.html', {'projects': projects})


@login_required
def assign_developers(request, project_id):
    if request.user.role != 'lead':
        return redirect('dashboard')

    project = get_object_or_404(Project, id=project_id)
    developers = CustomUser.objects.filter(role='developer')

    if request.method == 'POST':
        selected = request.POST.getlist('developers')
        Assignment.objects.filter(project=project).delete()
        for dev_id in selected:
            Assignment.objects.create(project=project, developer_id=dev_id)
        return redirect('dashboard')

    assigned = project.assignment_set.values_list('developer_id', flat=True)
    return render(request, 'core/assign.html', {
        'project': project, 'developers': developers, 'assigned': assigned
    })


# ========================
# Documents
# ========================

@login_required
def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.uploaded_by = request.user
            document.save()
            return redirect('dashboard')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form})


@login_required
def view_documents(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    documents = Document.objects.filter(project=project)
    return render(request, 'documents.html', {'project': project, 'documents': documents})
