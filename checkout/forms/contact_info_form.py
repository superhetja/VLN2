from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(label="Full name", max_length=120)
    street_name = forms.CharField(label="Street name", max_length=120)
    house_number = forms.CharField(label="House number", max_length=4)
    postal_code = forms.CharField(label="Postal code", max_length=20)
    city = forms.CharField(label="City", max_length=120)
    country = forms.CharField(label="Country", max_length=120)
