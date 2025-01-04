from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.user_login, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),   
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