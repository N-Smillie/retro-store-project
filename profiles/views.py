from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserProfileForm

from .models import UserProfile
from checkout.models import Order

@login_required
def profile(request):

    profile = request.user.profile

    if request.method == 'POST':

        form = UserProfileForm(
            request.POST,
            instance=profile
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Default shipping updated successfully.'
            )

            return redirect('profile')

    else:

        form = UserProfileForm(instance=profile)


    orders = profile.user.orders.all().order_by('-created_at')

    context = {
        'profile': profile,
        'form': form,
        'orders': orders,
    }

    return render(request, 'profiles/profile.html', context)
