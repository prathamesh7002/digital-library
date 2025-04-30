from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login , logout
# Create your views here.

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_dashboard')
    else:
        initial_data ={ 'username': '','password1': '','password2': ''}
        form = UserCreationForm(initial=initial_data)
        
    return render(request, 'users/register.html', {'form': form})   




def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user_dashboard')
    else:
        initial_data ={ 'username': '','password': ''}
        form = AuthenticationForm(initial=initial_data)
        
    return render(request, 'users/login.html', {'form': form})   


def user_logout(request):
    logout(request)
    return redirect('user_login')

def user_dashboard(request):
    return render(request, 'users/dashboard.html')


def user_profile(request):
    return render(request, 'users/profile.html')  # Render a profile template