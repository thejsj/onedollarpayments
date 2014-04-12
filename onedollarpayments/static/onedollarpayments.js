$(document).ready(function(){

	Stripe.setPublishableKey('pk_test_TfBx6CoDs9hB3ChWR0nf8AsJ');

	$request_form = $("#main-payment-request-form");

	if( $request_form.length > 0 ){

		console.log( 'Request Form Preset' );

		$request_form_inputs = $request_form.find("input");

		console.log( $request_form_inputs.length );
		console.log( $request_form_inputs );

		$request_form.find("input[type=submit]").click(function(e){

			e.preventDefault(); 
			
			console.log( 'Input Changed' );

			submitStripe(function(response){
				if( response !== false ){
					console.log( response );
					$request_form.find("#id_stripe_token-stripe_id").val( response.id );
					$request_form.find("#id_stripe_token-livemode").val( response.livemode );
					$request_form.find("#id_stripe_token-created").val( response.created );
					$request_form.find("#id_stripe_token-used").val( response.used );
					console.log( 'Form Submitted' );
					$request_form.submit();
				}	
				else {
					console.log( 'bad rsponse' );
				}
			});

			
		});
	}	
});

function submitStripe(callback){
	Stripe.card.createToken({
		number: $('#id_recepient-number').val(),
		cvc: $('#id_recepient-cvc').val(),
		exp_month: $('#id_recepient-exp_month').val(),
		exp_year: $('#id_recepient-exp_year').val(),
		country: 'US'
	}, function( code, response ){
		if( code === 200 ){
			console.log( response );
			callback(response);
		}
		else {
			callback(false);
		}
	});
}