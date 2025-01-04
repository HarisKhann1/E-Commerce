from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegistrationForm, LoginForm, PasswordResetForm
from .models import Category, Product
from django.core.mail import send_mail


# Create your views here.
def index(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')

    if category_id:
        products = Product.objects.filter(sub_category_id = category_id).order_by('-id')
        if not products:
           products = Product.objects.all()[:6] 
    else:
        products = Product.objects.all()[:6]
    
    context = {
        'categories': categories,
        'products': products
    }
    
    return render(request, 'index.html', context)


def signup(request):
    message = None
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')

            User.objects.create_user(username=username, email=email, password=password)
            message  = f"{username} has been registered successfully"
            return redirect('signin')
    else:
        form = RegistrationForm()
    return render(request, 'Auth/signup.html', {'form': form, 'message': message})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Authenticate using email
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in.")
                return redirect('/')  # Redirect to your home page or dashboard
            else:
                messages.error(request, "Invalid email or password.")
        else:
            messages.error(request, "Please fill in valid information.")
    else:
        form = LoginForm()
    return render(request, 'Auth/login.html', {'form': form, 'messages': messages})


"""

def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.get(email=email)
            print(user)
            if user:
                # Send email to user
                send_mail(
                    "Testing Email",
                    "This is a test email",
                    "seyamkhann4@gmail.com",
                    ["{email}"],
                    fail_silently=False,
                )
                messages.success(request, "Password reset link has been sent to your email.")
                print("Messages", messages)
            else:
                messages.error(request, "Email does not exist.")
        else:
            messages.error(request, "Please fill in valid information.")
    else:
        form = PasswordResetForm()
    return render(request, 'Auth/password_reset.html', {'form': form, 'messages': messages})

def password_reset_confirm(request):
    return render(request, 'Auth/password_reset_confirm.html')




"""