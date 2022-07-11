from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import ContactForm


def contact(request):
    """
    Shows and submits the contact form.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,
                             ('You successfuly submitted a message! '
                              'We will be in contact with you soon. '
                              'Thank you for reaching out!'))
            return redirect(reverse('query'))
        else:
            messages.error(request,
                           ('Failed to submit message. '
                            'Please ensure the form is valid.'))
    else:
        form = ContactForm()

    template = 'contact/contact.html/'

    context = {
        'form': form,
    }

    return render(request, template, context)
