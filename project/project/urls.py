from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from allauth.account.views import SignupView, LoginView, PasswordResetView

class MySignupView(SignupView):
    template_name = 'signup.html'

class MyLoginView(LoginView):
    template_name = 'login.html'

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('accounts/', include('allauth.socialaccount.urls')),
    path("", TemplateView.as_view(template_name="home.html")),

    path(r'^accounts/login', MyLoginView.as_view(), name='account_login'),
    path(r'^accounts/signup', MySignupView.as_view(), name='account_signup'),
]
