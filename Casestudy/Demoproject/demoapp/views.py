from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from .models import ErrorLog
from demoapp.form import UserRegisterForm, UserLoginForm


# Create your views here.
def homeview(request):
    return render(request,'demoapp/home.html')

def login_view(request):
    if request.method=="POST":
        loginform=UserLoginForm(data=request.POST)
        if loginform.is_valid():
            user = loginform.get_user()
            login(request, user)
            # Redirect to a specific page after login
            return redirect('home')

    loginform = UserLoginForm()
    return render(request, 'demoapp/login.html', {'form': loginform})
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'demoapp/register.html', {'form': form})

def logout_view(request):
    logout(request)
    # Redirect to a specific page after logout (e.g., home page)
    return redirect('home')

def capture_error(request):
    if request.method == 'POST':
        # Capture screenshots and record screen if possible
        # Log error details
        error_log = ErrorLog.objects.create(user=request.user)

        return render(request, 'demoapp/error_reported.html')
    else:
        return render(request, 'demoapp/error_report_form.html')