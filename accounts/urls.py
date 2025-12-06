from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),

    # Зміна пароля
    path('password_change/', 
         auth_views.PasswordChangeView.as_view(template_name='accounts/password_change_form.html'), 
         name='password_change'),
    path('password_change/done/', 
         auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), 
         name='password_change_done'),

    # Вихід
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
