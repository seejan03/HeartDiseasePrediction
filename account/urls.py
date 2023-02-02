from django.urls import path
from .views import Login
from . import views
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('login/',Login.as_view(),name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('reset_password',auth_views.PasswordResetView.as_view(template_name='account/Forgetpassword/password_reset.html'),name='reset_password'),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name='account/Forgetpassword/password_reset_sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='account/Forgetpassword/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name='account/Forgetpassword/password_reset_complete.html'),name='password_reset_complete'),
]