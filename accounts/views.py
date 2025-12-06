from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import ProfileEditForm



# -----------------------
# РЕЄСТРАЦІЯ (function-based)
# -----------------------
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # автоматичний логін після реєстрації
            return redirect('profile')
    else:
        form = UserRegistrationForm()

    return render(request, "accounts/register.html", {'form': form})


# -----------------------
# ПРОФІЛЬ
# -----------------------
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')   # якщо файл у /templates/profile.html


@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=request.user)

    return render(request, 'accounts/profile_edit.html', {'form': form})
    

# -----------------------
# ЛОГІН / ЛОГАУТ
# -----------------------
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    form_class = AuthenticationForm


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')


# -----------------------
# РЕЄСТРАЦІЯ (class-based)
# -----------------------
class RegisterView(CreateView):
    model = User
    template_name = "accounts/register.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
