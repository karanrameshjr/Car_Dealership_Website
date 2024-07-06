from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

from .forms import UserRegistrationForm, UserLoginForm  # Import your custom forms here

# Your existing registration and login views
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Create a user account here
            # Example:
            # username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            # password = form.cleaned_data['password']
            # user = User.objects.create_user(username, email, password)
            return redirect('user_login')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a dashboard or another page after login
                return redirect('dashboard')
            else:
                # Handle invalid login credentials
                pass
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

# Additional registration view using Django's built-in UserCreationForm
def register_builtin(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('home')  # Redirect to your home page or any other page
    else:
        form = UserCreationForm()
    return render(request, 'homepage/register.html', {'form': form})

# Additional views from your second set of code
def home(request):
    # Your logic goes here
    return render(request, 'home/home.html')

def index_view(request):
    # Your logic goes here
    return render(request, 'home/index.html')
