from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

  
PAYMENT = (
    ('C', 'Credit Card'),
    ('D', 'Debit Card')
)

class CheckoutForm(forms.Form):
	class Meta:
		street_address = forms.CharField(widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': '1234 Main St.'
		}))
		apartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Apartment or suite'
		}))
		country = CountryField(blank_label='(select country)').formfield(widget=CountrySelectWidget(attrs={
			'class': 'custom-select d-block w-100'
		}))
		zip = forms.CharField(widget=forms.TextInput(attrs={
			'class': 'form-control'
		}))
		same_billing_address = forms.BooleanField(required=False)
		save_info = forms.BooleanField(required=False)
		payment_option = forms.ChoiceField(
			widget=forms.RadioSelect, choices=PAYMENT
		)