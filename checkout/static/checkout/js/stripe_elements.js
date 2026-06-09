document.addEventListener('DOMContentLoaded', function() {

    var form = document.getElementById('payment-form');
    var submitButton = document.getElementById('submit-button');
    var errorDiv = document.getElementById('card-errors');

    var stripePublicKey = JSON.parse(
        document.getElementById('id_stripe_public_key').textContent
    );

    var clientSecret = JSON.parse(
        document.getElementById('id_client_secret').textContent
    );

    var stripe = Stripe(stripePublicKey);
    var elements = stripe.elements();

    var card = elements.create('card');
    card.mount('#card-element');

    form.addEventListener('submit', async function(event) {

        event.preventDefault();

        card.update({ disabled: true });
        submitButton.disabled = true;

        document
            .getElementById('loading-overlay')
            .classList.remove('d-none');

        const result = await stripe.confirmCardPayment(
            clientSecret,
            {
                payment_method: {
                    card: card,
                    billing_details: {
                        name: form.full_name.value.trim(),
                        email: form.email.value.trim(),
                        phone: form.phone_number.value.trim(),
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

            document
                .getElementById('loading-overlay')
                .classList.add('d-none');

            errorDiv.textContent = result.error.message;

            card.update({ disabled: false });
            submitButton.disabled = false;

        } else if (result.paymentIntent.status === 'succeeded') {

            form.submit();
        }
    });

});