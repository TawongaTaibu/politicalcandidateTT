from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import CreateUserForm
from .models import News
from datetime import datetime


# This function holds the Data-driven component of our webpage
def home(request):
    global_warming_data = {
        'temperature_rise': '1.1°C',
        'sea_level_rise': '20cm',
        'co2_levels': '419 ppm'
    }
    return render(request, 'home.html', {'global_warming_data': global_warming_data})

#This function handles the user's login process
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('News')  #Redirect to the news page after successful login
        else:
            messages.error(request, "Invalid username or password.")  #Display an error message for invalid login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# This function handles the user's registration process and it uses a form to do so
def registration(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dfa:login')
    else:
        form = CreateUserForm()
    return render(request, 'registration.html', {'form': form})

# Firstly, a user has to be logged in to be able to access the News page
@login_required
def News_View(request, id):
    selected_news = get_object_or_404(News,id=id)
    return render(request, 'News_View.html', {'selected_news':selected_news})

def news_list(request):
    news_items = News.objects.all()
    return render(request, 'news_list.html', {'news_items':news_items})
