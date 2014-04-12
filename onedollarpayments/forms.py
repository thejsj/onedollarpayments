from django import forms
from onedollarpayments.models import *
from django.forms.widgets import HiddenInput, NumberInput

# Forms for request

class RequestSenderForm(forms.ModelForm):

    class Meta:
        model = Sender
        fields = ['email', 'bank_routing_number', 'bank_account_number']

    def __init__(self, *args, **kwargs):
        super(RequestSenderForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = "Your Email Address"
        self.fields['bank_routing_number'].label = "Your Bank Routing Number"
        self.fields['bank_account_number'].label = "Your Bank Account Number"

class RequestRecepientForm(forms.ModelForm):
    class Meta:
        model = Recepient
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super(RequestRecepientForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = "Recepient's Email Address"

class RequestPaymentRequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['quantity']

    def __init__(self, *args, **kwargs):
        super(RequestPaymentRequestForm, self).__init__(*args, **kwargs)
        self.fields['quantity'].label = "Payment Amount (in USD)"



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
