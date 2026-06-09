from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserProfile
from checkout.models import Order

@login_required
def profile(request):

    profile = request.user.profile

    orders = profile.user.orders.all().order_by('-created_at')

    context = {
        'profile': profile,
        'orders': orders,
    }

    return render(request, 'profiles/profile.html', context)
