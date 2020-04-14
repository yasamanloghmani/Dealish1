from django.urls import path
from . import views

urlpatterns = [
    path('accounts/signup/', views.signup, name="signup"),
    path('main/', views.main, name='main'),
    path('favorits/', views.favorits, name='favorits'),
    path('restaurant/', views.restaurant, name='restaurant'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
]