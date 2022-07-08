from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_shopping_bag(request):
    """A view to return the shopping bag page"""
    return render(request, 'shopping_bag/shopping_bag.html')


def add_to_bag(request, item_id):
    """Add the quantity of the product specified to the shopping bag"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(request, (
                    f'You updated the number of {size.upper()} {product.name} \
                        in your shopping bag to \
                            {bag[item_id]["items_by_size"][size]}'
                ))
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(request, (
                    f'You added {size.upper()} {product.name} to your \
                        shopping bag'
                ))
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, (
                f'You added {size.upper()} {product.name} to your shopping bag'
            ))
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, (
                f'You updated the number of {product.name} in your shopping \
                    bag to {bag[item_id]}'
            ))
        else:
            bag[item_id] = quantity
            bag[item_id] = quantity
            messages.success(request, (
                f'You added {product.name} to your shopping bag'
            ))

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request, (
                f'You updated the number of {size.upper()} {product.name} \
                    in your shopping bag to \
                        {bag[item_id]["items_by_size"][size]}'
            ))
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
                messages.success(request, (
                    f'You removed {size.upper()} {product.name} from your \
                        shopping bag'
                ))
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, (
                f'You updated the number of {product.name} in your shopping \
                    bag to {bag[item_id]}'
            ))
        else:
            bag.pop(item_id)
            messages.success(request, (
                f'You removed {product.name} from your shopping bag'
            ))

    request.session['shopping_bag'] = bag
    return redirect(reverse('view_shopping_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    product = get_object_or_404(Product, pk=item_id)
    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, (
                f'You removed {size.upper()} {product.name} from your \
                    shopping bag'
            ))
        else:
            bag.pop(item_id)
            messages.success(request, (
                f'You removed {product.name} from your shopping bag'
            ))

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
