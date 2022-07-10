from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from checkout.models import Order
from .models import UsersProfile
from .forms import UsersProfileForm


@login_required
def profile(request):
    """
    Renders the profile page
    """
    profile = get_object_or_404(UsersProfile, user=request.user)
    orders = profile.orders.all()
    form = UsersProfileForm(instance=profile)
    if not profile:
        messages.error(request,
                       "I'm sorry, you need to log in first")
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = UsersProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """
    Renders the order history
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past order confirmation for order number {order_number}.'
    ))

    template = 'checkout/checkout_successful.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
