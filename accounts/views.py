from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def account(request):
    profile = request.user.profile
    days_left = 75 - profile.days_since_registration  # Вычисляем оставшиеся дни
    if profile.days_since_registration >= 76:
        return render(request, 'accounts/account_blocked.html')
    return render(request, 'accounts/account.html', {
        'profile': profile,
        'days_left': days_left  # Передаем результат в шаблон
    })

from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)
    return redirect('home')  