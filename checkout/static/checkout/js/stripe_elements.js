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