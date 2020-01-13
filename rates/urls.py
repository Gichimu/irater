from django.urls import path
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from allauth.account.views import SignupView, LoginView
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    # url(r'^accounts/signup', SignupView.as_view(), name = 'account_signup'),
    # url(r'^accounts/login', views.login, name = 'account_login'),
    url(r'^accounts/changepassword', views.changePassword, name = 'change_password'),
    url(r'^accounts/resetpassword', views.resetPassword, name = 'account_reset_password'),
    url(r'^profile/(?P<user_id>\d+)', views.profile, name = 'profile'),
    url(r'^edit/profile', views.update_profile, name = 'update_profile'),
    url(r'^create/post', views.create_post, name = 'create_posts'),

] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

