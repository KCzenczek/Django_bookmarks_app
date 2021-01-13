from django.urls import path
from . import views


urlpatterns = [
    # widoki logowania
    path('login/', views.user_login, name='login'),
]
