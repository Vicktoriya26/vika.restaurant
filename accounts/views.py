
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('menu:product_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        # просте оновлення даних
        request.user.email = request.POST.get('email', request.user.email)
        request.user.phone = request.POST.get('phone', request.user.phone)
        request.user.address = request.POST.get('address', request.user.address)
        request.user.save()
        return redirect('profile')
    return render(request, 'accounts/profile.html')

