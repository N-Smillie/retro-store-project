from django import forms

from .models import UserProfile


class UserProfileForm(forms.ModelForm):

    class Meta:

        model = UserProfile

        fields = [
            'default_phone_number',
            'default_street_address1',
            'default_street_address2',
            'default_town_or_city',
            'default_postcode',
            'default_county',
            'default_country',
        ]

        widgets = {

            'default_phone_number':
                forms.TextInput(
                    attrs={
                        'class':'form-control'
                    }
                ),

            'default_street_address1':
                forms.TextInput(
                    attrs={
                        'class':'form-control'
                    }
                ),

            'default_street_address2':
                forms.TextInput(
                    attrs={
                        'class':'form-control'
                    }
                ),

            'default_town_or_city':
                forms.TextInput(
                    attrs={
                        'class':'form-control'
                    }
                ),

            'default_postcode':
                forms.TextInput(
                    attrs={
                        'class':'form-control'
                    }
                ),

            'default_county':
                forms.TextInput(
                    attrs={
                        'class':'form-control'
                    }
                ),

            'default_country':
                forms.TextInput(
                    attrs={
                        'class':'form-control'
                    }
                ),
        }