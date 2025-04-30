from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

@login_required
def user_dashboard(request):
    return render(request, 'users/dashboard.html')
