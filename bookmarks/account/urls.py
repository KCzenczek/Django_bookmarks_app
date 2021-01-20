from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # poprzedni widok logowania
    # path('login/', views.user_login, name='login'),
    # wbudowany
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
    # adresy przeznaczone do obsługi zmiany hasła; nie trzeba nic forms.py ani wiews.py
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path(
        'password_change/done',
        auth_views.PasswordChangeDoneView.as_view(),
        name='password_change_done'
    ),
    # adresy url przenaczone do obsługi procedury zerowania hasła
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path(
        'password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),
]
