from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm


def register(request):
    """Реєстрація нового користувача"""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('menu:product_list')
        else:
            messages.error(request, "Будь ласка, виправте помилки у формі.")
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    """Логін користувача"""
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('menu:product_list')
        else:
            messages.error(request, "Неправильний логін або пароль.")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def user_logout(request):
    """Вихід користувача"""
    logout(request)
    return redirect('accounts:login')


@login_required
def profile(request):
    """Перегляд профілю користувача"""
    return render(request, 'accounts/profile.html')


@login_required
def profile_edit(request):
    """Редагування профілю користувача"""
    if request.method == 'POST':
        email = request.POST.get('email', request.user.email)
        phone = request.POST.get('phone', getattr(request.user, 'phone', ''))
        address = request.POST.get('address', getattr(request.user, 'address', ''))

        request.user.email = email
        request.user.phone = phone
        request.user.address = address
        request.user.save()

        messages.success(request, "Профіль успішно оновлено!")
        return redirect('accounts:profile')

    return render(request, 'accounts/profile_edit.html', {
        'email': request.user.email,
        'phone': getattr(request.user, 'phone', ''),
        'address': getattr(request.user, 'address', ''),
    })
