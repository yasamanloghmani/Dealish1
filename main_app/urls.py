from django.urls import path
from . import views

urlpatterns = [
    path('accounts/signup/', views.signup, name="signup"),
    path('about/', views.about, name='about')
]