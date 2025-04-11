from django.urls import path
from . import views
from .views import recommendation_view


urlpatterns = [
    path('',views.Home, name='home'),
    path('register/',views.RegisterView, name='register'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('forgot_password/', views.ForgotPassword, name='forgot-password'),
    path('password-reset-sent/<str:reset_id>/', views.PasswordResetSent, name='password-reset-sent' ),
    path('reset-password/<str:reset_id>/', views.ResetPassword, name='reset-password'),
    path('match/', views.profile_match_view, name='profile_match'),
    path('recommendations/', recommendation_view, name='recommendations'),
]
