from django.db import models

CONTACT_CHOICES = {
    ('REQUEST_CALL_BACK', 'Yes'),
    ('NO_REQUEST_CALL_BACK', 'No'),
}


class Contact(models.Model):
    """
    Contact Model
    """
    name = models.CharField(max_length=254)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30, blank=True)
    request_call_back = models.CharField(
        max_length=20, choices=CONTACT_CHOICES)
    message = models.TextField()
    contact_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
