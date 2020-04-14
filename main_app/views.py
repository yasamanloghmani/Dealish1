from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def signup(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('deals_index')
    context = {'form': form} 
    return render(request, 'registration/signup.html', context)

def main(request):
    return render(request, 'mainpage.html')

def favorits(request):
    return render(request, 'favorits.html')

def restaurant(request):
    return render(request, 'restaurant.html')

def profile(request):
    return render(request, 'profile.html')

def about(request):
    return render(request, 'about.html')