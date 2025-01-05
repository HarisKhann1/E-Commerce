from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.user_login, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('contact/', views.contact, name='contact'),
    path('order/', views.order, name='order'),
    path('user-orders/', views.user_orders, name='user_orders'),

    # card urls
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),   
]

'''
    #  Sends the password reset email with a token link.
    path('password_reset/', views.password_reset, name='password_reset'), 
    #  Displays a message confirming the reset email was sent.
    path('password_reset/done/', views.password_reset_confirm, name='password_reset_done'),
    # Allows the user to reset their password after clicking the reset link.
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # # Displays a success message after the password is reset.
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
'''