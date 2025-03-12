from django.shortcuts import redirect
from django.urls import reverse

def not_blocked(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.profile.days_since_registration >= 76:
            return redirect(reverse('account'))
        return view_func(request, *args, **kwargs)
    return wrapper