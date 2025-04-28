from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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