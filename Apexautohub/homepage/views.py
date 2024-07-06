from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView
from .forms import ContactForm, UserRegistrationForm

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'home/user_register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Change 'home' to the URL name of your home page
            else:
                # Handle invalid login credentials
                pass
    else:
        form = AuthenticationForm()
    response = render(request, 'home/user_login.html', {'form': form})
    response['Cache-Control'] = 'no-store'
    return response

@login_required
def profile_view(request):
    return render(request, 'home/profile.html', {'user': request.user})

def home(request):
    return render(request, 'home/home.html')

def index_view(request):
    return render(request, 'home/index.html')

def contact_form_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to a success page
    else:
        form = ContactForm()
    
    return render(request, 'index.html', {'form': form})
