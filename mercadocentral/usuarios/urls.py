from django.urls import path
from .views import AltaView #, PerfilUpdateView, PerfilEmailView
from django.contrib.auth.views import LoginView, PasswordResetView

usuarios_patterns = [
    
    path('login/', LoginView.as_view(template_name='usuarios/login.html'), name='usu_login'),
    path('pwd/', PasswordResetView.as_view(template_name='usuarios/password_reset_form.html'), name='usu_password_reset'),
    path('register/', AltaView.as_view(), name='usu_alta'),
#    path('signup/', AltaView.as_view(), name='signup'),
#    path('profile/', PerfilUpdateView.as_view(), name='profile'),
#    path('profile/email/', PerfilEmailView.as_view(), name='profile_email'),

]