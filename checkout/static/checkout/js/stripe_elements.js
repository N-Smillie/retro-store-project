var stripePublicKey = JSON.parse(
    document.getElementById('id_stripe_public_key').textContent
);

var clientSecret = JSON.parse(
    document.getElementById('id_client_secret').textContent
);

var stripe = Stripe(stripePublicKey);

var elements = stripe.elements();

var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

var card = elements.create('card', {style: style});

card.mount('#card-element');

// Handle form submit
form.addEventListener(
    'submit',
    async function(event) {

        event.preventDefault();

        card.update({ disabled: true });

        submitButton.disabled = true;

        const result =
            await stripe.confirmCardPayment(
                clientSecret,
                {
                    payment_method: {
                        card: card,
                        billing_details: {
                            name: form.full_name.value.trim(),
                            phone: form.phone_number.value.trim(),
                            email: form.email.value.trim(),
                        }
                    },
                    shipping: {
                        name: form.full_name.value.trim(),
                        phone: form.phone_number.value.trim(),
                        address: {
                            line1: form.street_address1.value.trim(),
                            line2: form.street_address2.value.trim(),
                            city: form.town_or_city.value.trim(),
                            country: form.country.value.trim(),
                            postal_code: form.postcode.value.trim(),
                            state: form.county.value.trim(),
                        }
                    }
                }
            );

        if (result.error) {

            errorDiv.textContent =
                result.error.message;

            card.update({ disabled: false });

            submitButton.disabled = false;

        } else if (
            result.paymentIntent.status ===
            'succeeded'
        ) {

            form.submit();

        }
    }
);