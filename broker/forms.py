from django import forms
from .models import Broker


class BrokerForm(forms.ModelForm):

    class Meta:
        model = Broker
        fields = [
            'name',
            'email',
            'phone',
            'picture',
        ]

        labels = {
            'name': "Name",
            'email': "Email",
            'phone': "Phone",
            'picture': "Picture",
        }

        help_texts = {
            'name': "Enter the name of the broker.",
            'email': "Enter the email of the broker.",
            'phone': "Enter the phone of the broker.",
            'picture': "Upload a picture of the broker.",
        }