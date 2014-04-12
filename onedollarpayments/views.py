from django.http import HttpResponse
from django.shortcuts import *
from django.core.urlresolvers import reverse
from django.conf import settings

from onedollarpayments.models import *
from onedollarpayments.forms import *
from onedollarpayments.functions import *

import stripe

# Email
from django.core.mail import send_mail

def home(request):

    # Initalize our two forms here with separate prefixes
    sender_form    = RequestSenderForm(prefix="sender")
    recepient_form = RequestRecepientForm(prefix="recepient")
    request_form   = RequestPaymentRequestForm(prefix="request")

    # Check to see if a POST has been submitted. Using GET to submit forms?
    # Don't do it. Use POST.
    if request.POST:
        # Load up our two forms again using the prefix keyword argument.
        sender_form    = RequestSenderForm(request.POST,prefix="sender")
        recepient_form = RequestRecepientForm(request.POST,prefix="recepient")
        request_form   = RequestPaymentRequestForm(request.POST,prefix="request")

        # Ensure both forms are valid before continuing on
        if sender_form.is_valid() and recepient_form.is_valid() and request_form.is_valid():
            # Prepare the school model, but don't commit it to the database
            # just yet.
            request_form = request_form.save(commit=False)

            # Add the location ForeignKey by saving the secondary form we
            # setup
            request_form.sender = sender_form.save()
            request_form.recepient = recepient_form.save()

            # raise Exception( request_form.__dict__ )

            # Save the main object and continue on our merry way.
            request_form.save()

            # Send Email To Recepient
            send_mail(
                'Money Request Received', 
                '%s has send you money request for $%s\n\nVisit the following link in order to make this payment:\n\nhttp://1dollarpayments.thejsj.com%s' % (
                    request_form.recepient, 
                    request_form.quantity, 
                    
                    reverse('recepient_pay_request', kwargs = {'payment_request_hash': request_form.id}),
                ), 
                request_form.sender.email,
                [request_form.recepient.email], 
                fail_silently=False
            )

            # Send Email To Recepient
            send_mail(
                'Money Request Sent', 
                'Your Payment Has Been Sent to %s for $%s' % (
                    request_form.recepient, 
                    request_form.quantity, 
                ), 
                request_form.sender.email,
                [request_form.sender.email], 
                fail_silently=False
            )

            return render(request, 'confirmation.html', {
                'request_form': request_form,
            })

    return render(request, 'request.html', {
        'sender_form': sender_form,
        'recepient_form': recepient_form,
        'request_form': request_form,
    })

def recepient_pay_request(request, payment_request_hash ):

    
    # Check to see if a POST has been submitted. Using GET to submit forms?
    # Don't do it. Use POST.
    if request.POST:

        payment_request = get_object_or_404( Request, pk=payment_request_hash )

        # Load up our two forms again using the prefix keyword argument.
        recepient_form    = PaymentRecepientForm(request.POST,prefix="recepient")
        stripe_token_form = StripeTokenForm(request.POST,prefix="stripe_token")

        # Ensure both forms are valid before continuing on
        if recepient_form.is_valid() and stripe_token_form.is_valid():

            payment_request.recepient.stripe_token = stripe_token_form.save()
            payment_request.recepient.save()

            # Stripe Stuff
            stripe.api_key = "sk_test_0KVbveRNHYURQQbsqBWMWgFL"

            # Check For Stripe
            stripe_charge = stripe.Charge.create(
                amount=int(payment_request.quantity * 100),
                currency="usd",
                card=payment_request.recepient.stripe_token.stripe_id, # obtained with Stripe.js
                description="Charge for %s" % ( payment_request.sender.email )
            )

            send_mail(
                'Payment Succesful!', 
                'Your Payment to %s has been succseful.' % (
                    payment_request.sender.email, 
                ), 
                payment_request.recepient.email,
                [payment_request.recepient.email], 
                fail_silently=False
            )

            send_mail(
                'Payment Received!', 
                '%s has completed your payment request for %s. Now go spend those dolla billz!' % (
                    payment_request.recepient.email, 
                    payment_request.quantity, 
                ), 
                payment_request.sender.email,
                [payment_request.sender.email], 
                fail_silently=False
            )
            
            return render(request, 'payment-request-confirmation.html', {
                'payment_request': payment_request,
                'recepient_form': recepient_form,
                'stripe_token_form': stripe_token_form,
                'stripe_charge': stripe_charge,
            })

    payment_request = get_object_or_404( Request, pk=payment_request_hash )

    # Initalize our two forms here with separate prefixes
    recepient_form = PaymentRecepientForm(prefix="recepient")
    stripe_token_form = StripeTokenForm(prefix="stripe_token")

    return render(request, 'payment-request.html', {
        'payment_request': payment_request,
        'recepient_form': recepient_form,
        'stripe_token_form': stripe_token_form,
        # 'credic_card_info_form': credic_card_info_form,
    })


