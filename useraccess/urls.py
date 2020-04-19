from django.contrib import admin
from django.urls import path, include
from .views import HomeView, SignupView, ProfileView

urlpatterns = [
    path('', HomeView.as_view(), name="home" ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignupView.as_view(), name="signup"),
    path('profile/', ProfileView.as_view(), name="profile")
]

