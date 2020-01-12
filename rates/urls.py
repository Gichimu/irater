from django.urls import path
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from allauth.account.views import SignupView, LoginView
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    url(r'^accounts/signup', SignupView.as_view(), name = 'account_signup'),
    url(r'^accounts/login', views.login, name = 'account_login'),
    url(r'^accounts/changepassword', views.changePassword, name = 'change_password'),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

