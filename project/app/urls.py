from django.urls import path
from . import views 
from django import forms
from django.urls import path
from django.utils.translation import templatize
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm , MySetPasswordForm

urlpatterns = [
        path('', views.index,name='index'),
        
        path('accounts/login/',auth_views.LoginView.as_view(template_name = 'login.html',authentication_form = LoginForm ),name = 'login'),
        path('logout/',auth_views.LogoutView.as_view(next_page = 'login'),name='logout'),
        path('changepassword/',auth_views.PasswordChangeView.as_view(template_name='changepassword.html',form_class=MyPasswordChangeForm , success_url = '/changepasswordDone/'),name='changepassword'),
        path('changepasswordDone/',auth_views.PasswordChangeView.as_view(template_name='changepasswordDone.html'),name='changepasswordDone'),
        path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html' ,form_class = MyPasswordResetForm , ),name='password-reset'),
        path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
        path('password_reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',form_class = MySetPasswordForm),name='password_reset_confirm'),
        path('password_reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
        path('accounts/profile/',views.profile,name='profile'),
        path('registration/', views.CustomerRegistrationView.as_view(), name='register'),
        path('test',views.test,name='test'),
        
        path('about',views.about,name='about'),

        path('roadmap/<str:career>',views.roadmap,name='roadmap'),
        path('courses/<str:career>',views.courses,name='courses'),


                

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
