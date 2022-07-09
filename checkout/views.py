from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.conf import settings
from .models import OrderLineItem, Order
from .forms import OrderForm
from shopping_bag.contexts import bag_contents

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                            order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
            )
                            order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the items in your shopping bag was not found \
                            in our database. "
                        "Please call our customer service for assistance.")
            )
                    order.delete()
                    return redirect(reverse('view_shopping_bag'))

            request.session['save_info'] = 'save_info' in request.POST
            return redirect(reverse('checkout_successful',
                            args=[order.order_number]))
        else:
            messages.error(request, 'There was an issue with your order.\
                Please check your order information and try again.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request,
                           "There's nothing in your shopping bag right now")
            return redirect(reverse('products'))
        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
                Did you forget to set this in your environment?')

        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)


def checkout_successful(request, order_number):
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    messages.success(request, f'Your order has been successfully processed. \
        You order number is {order_number}. A confirmation email will be sent \
            to your email {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_successful.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
