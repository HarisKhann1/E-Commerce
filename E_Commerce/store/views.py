from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegistrationForm, LoginForm, PasswordResetForm
from .models import Category, Product, Contact, Order, Brand
from django.core.mail import send_mail

from django.contrib.auth.decorators import login_required
from cart.cart import Cart

# Create your views here.
def index(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()
    brand_id = request.GET.get('brand')
    range = request.GET.get('range')
    
    print(range)
    category_id = request.GET.get('category')
    if category_id:
        products = Product.objects.filter(sub_category_id = category_id).order_by('-id')
        if not products:
           products = Product.objects.all()[:6]
    elif brand_id: 
        products = Product.objects.filter(brand_id = brand_id).order_by('-id')
        if not products:
            products = Product.objects.all()[:6]
    else:
        products = Product.objects.all()[:6]
    
    context = {
        'categories': categories,
        'products': products,
        'brands': brands

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
    return render(request, 'Auth/login.html', {'form': form})

# order views logic here
@login_required(login_url="/signin")
def order(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        card = request.session.get('cart');
        u_id = request.user.id
        user = User.objects.get(id = u_id)
        if user:
            for key, value in card.items():
                product = Product.objects.get(id=key)
                quantity = value.get('quantity')
                price = value.get('price')
                total = float(price) * float(quantity) 
                
                Order.objects.create(user=user, product=product, quantity=quantity, price=price, total=total, phone=phone, address=address)
                cart_clear(request)
        messages.success(request, "Your order has been placed successfully.")
        return redirect('index')

# showing user orders
@login_required(login_url="/signin")
def user_orders(request):
    u_id = request.user.id
    orders = Order.objects.filter(user_id = u_id)

    order_data = []
    for order in orders:
        image = order.product.image
        name = order.product.name
        price = order.price
        quantity = order.quantity
        total = order.total

        order_data.append({
            'image': image,
            'name': name,
            'price': price,
            'quantity': quantity,
            'total': total
        })
    
    context = {'order_data': order_data}
   
        
    return render(request, 'cart/user_orders.html', context)


# card views logic here
@login_required(login_url="/signin")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect('index')

@login_required(login_url="/signin")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/signin")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/signin")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/signin")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/signin")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contact.objects.create(name=name, email=email, subject=subject, message=message)
        messages.success(request, "Your message has been sent successfully.")

        return redirect('contact')

    return render(request, 'contact/contact.html')

def product_detail(request, id=None):

    if id:
        product_info = Product.objects.get(id=int(id))
        
    else:
        product_info = None
        messages.error(request, "Product not found.")

    context = {
        'product_info': product_info
    }

    return render(request, 'Main/product_detail.html', context)


def search_product(request):
    search = request.GET.get('search')

    if search:
        products = Product.objects.filter(name__icontains=search)
    
    context = {
            'products': products,
            'search': search
        }
    return render(request, 'Main/search_product.html', context)
            




















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

