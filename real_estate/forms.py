from django import forms
from .models import RealEstate


class RealEstateForm(forms.ModelForm):

    class Meta:
        model = RealEstate
        fields = [
            'real_estate_type',
            'address',
            'area',
            'price',
            'description',
            'main_image',
            'broker',
            'feature',
        ]

        labels = {
            'area': "Area",
            'price': "Price",
            'address': "Address",
            'description': "Description",
            'real_estate_type': "Property type",
            'main_image': "Main image",
            'broker': "Broker",
            'feature': "Features",
        }

        help_texts = {
            'area': "Enter a number greater than zero.",
            'price': "Enter a number greater than zero.",
            'address': "Enter the complete address of the property.",
            'description': "Enter a description of the property.",
            'real_estate_type': "Choose the type of property.",
            'main_image': "Upload the main image of the property.",
            'broker': "Choose the broker for the property.",
            'feature': "Choose the features of the property.",
        }

        widgets = {
            'address': forms.TextInput(
                attrs={'placeholder': "For example Geo Milev str 22"}
            ),
            'area': forms.NumberInput(
                attrs={'placeholder': "Area in square meters"}
            ),
            'price': forms.NumberInput(
                attrs={'placeholder': "Price in euros"}
            ),
            'description': forms.Textarea(
                attrs={'placeholder': "Describe the property's condition"}
            ),
        }

    def clean_area(self):
        area = self.cleaned_data['area']

        if area <= 0:
            raise forms.ValidationError(
                'Area must be greater than zero.'
            )
        return area


    def clean_price(self):
        price = self.cleaned_data['price']

        if price <= 0:
            raise forms.ValidationError(
                'Price must be greater than zero.'
            )
        return price

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['address'].disabled = True