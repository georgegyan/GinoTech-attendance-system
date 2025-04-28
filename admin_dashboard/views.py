from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import AddUserForm

def dashboard_home(request):
    return render(request, 'admin_dashboard/dashboard_home.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard_home')
        else:
            return render(request, 'admin_dashboard/login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'admin_dashboard/login.html')

@login_required(login_url='/admin-dashboard/login/')
def dashboard_home(request):
    return render(request, 'admin_dashboard/dashboard_home.html')

@login_required(login_url='/admin-dashboard/login/')
def manage_users(request):
    users = User.objects.all()
    return render(request, 'admin_dashboard/manage_users.html', {'users': users})

def user_logout(request):
    logout(request)
    return redirect('user_login')

def add_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, f'User {username} created successfully!')
        return redirect('admin_dashboard:manage_users')

    return render(request, 'admin_dashboard/add_user.html')

def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            # Create the user
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  
            user.save()

            messages.success(request, 'User created successfully!')

            # Redirect to the success page or the dashboard after saving
            return redirect('admin_dashboard:add_user')

    else:
        form = AddUserForm()

    return render(request, 'admin_dashboard/add_user.html', {'form': form})