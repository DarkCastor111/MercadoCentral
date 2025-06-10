from django.urls import path
from . import views

footer_patterns = [
    path('detail/', views.footer_detail, name='footer_detail'),
]