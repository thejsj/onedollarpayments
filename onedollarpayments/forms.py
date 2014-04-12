from django import forms
from onedollarpayments.models import *
from django.forms.widgets import HiddenInput, NumberInput

# Forms for request

class RequestSenderForm(forms.ModelForm):

    class Meta:
        model = Sender
        fields = ['email', 'bank_routing_number', 'bank_account_number']

class RequestRecepientForm(forms.ModelForm):
    class Meta:
        model = Recepient
        fields = ['email']

class RequestPaymentRequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['quantity']

# Forms for payment

class PaymentRecepientForm(forms.ModelForm):

    number    = forms.IntegerField()
    cvc       = forms.IntegerField()
    exp_month = forms.IntegerField()
    exp_year  = forms.IntegerField()

    class Meta:
        model = Recepient
        fields = ['email', 'number', 'cvc', 'exp_month', 'exp_year']

class StripeTokenForm(forms.ModelForm):

    class Meta:
        model = StripeToken
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StripeTokenForm, self).__init__(*args, **kwargs)
        self.fields['stripe_id'].widget = HiddenInput()
        self.fields['livemode'].widget = HiddenInput()
        self.fields['created'].widget = HiddenInput()
        self.fields['used'].widget = HiddenInput()
