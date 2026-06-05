from django import forms
from .models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'full_name',
            'email',
            'phone_number',
            'street_address1',
            'street_address2',
            'town_or_city',
            'postcode',
            'county',
            'country',
        )

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['full_name'].widget.attrs[
            'autofocus'
        ] = True

        placeholders = {
            'full_name': 'Enter your full name',
            'email': 'Enter your email address',
            'phone_number': 'Enter your phone number',
            'street_address1': 'House number and street',
            'street_address2': '(optional)',
            'town_or_city': 'Town or city',
            'postcode': 'Postcode',
            'county': 'County (optional)',
            'country': 'Country',
        }

        for field in self.fields:
            self.fields[field].widget.attrs[
                'class'
            ] = 'form-control'

            if field in placeholders:
                self.fields[field].widget.attrs[
                    'placeholder'
                ] = placeholders[field]