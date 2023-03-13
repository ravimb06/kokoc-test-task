from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.urls import path

from profiles.views import SignUp

app_name = 'profiles'

urlpatterns = [
    path(
        'logout/',
        LogoutView.as_view(template_name='profiles/logged_out.html'),
        name='logout'
    ),
    path('signup/', SignUp.as_view(), name='signup'),
    path(
        'login/',
        LoginView.as_view(template_name='profiles/login.html'),
        name='login'
    ),
    path(
        'password_reset/',
        PasswordResetView.as_view(
            template_name='profiles/password_reset_form.html'
        ),
        name='password_reset'
    ),
    path(
        'password_reset/done/',
        PasswordResetDoneView.as_view(
            template_name='profiles/password_reset_done.html'
        ),
        name='password_reset_done'
    ),
    path(
        'password_change', PasswordChangeView.as_view(
            template_name='profiles/password_change_form.html'
        ),
        name='password_change'
    ),
    path(
        'password_change/done/',
        PasswordChangeDoneView.as_view(
            template_name='profiles/password_change_done.html'
        ),
        name='password_change_done'
    ),
]
