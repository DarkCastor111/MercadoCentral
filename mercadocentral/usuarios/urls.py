from django.urls import path
from .views import AltaView, UserChangeView #, PerfilEmailView
from django.contrib.auth import views as auth_views 



usuarios_patterns = [
    
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usuarios/login.html'), name='logout'),
    path('pwd_reset/', auth_views.PasswordResetView.as_view(template_name='usuarios/password_reset_form.html'), name='password_reset'),
    path('pwd_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='usuarios/password_reset_done.html'), name='password_reset_done'),
    path('pwd_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='usuarios/password_reset_confirm.html'), name='password_reset_confirm'),
    path('pwd_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='usuarios/password_reset_complete.html'), name='password_reset_complete'),
    path('pwd_chg/', auth_views.PasswordChangeView.as_view(template_name='usuarios/password_change_form.html'), name='password_change'),
    path('pwd_chg/done/', auth_views.PasswordChangeDoneView.as_view(template_name='usuarios/password_change_done.html'), name='password_change_done'),
    path('register/', AltaView.as_view(), name='usu_alta'),
    path('perso/', UserChangeView.as_view(), name='usu_perso'),
#    path('profile/email/', PerfilEmailView.as_view(), name='profile_email'),

]