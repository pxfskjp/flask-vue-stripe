<template>
	<section class="order-container">
		<header>
			<h1>Ready to rent?</h1>
		</header>
		<router-link to="/" class="button return">Back</router-link>
		<article>
			<!-- Note to self: research best practice- using this section with divs inside for structure, or the div on the outside with sections inside -->
			<section>
				<div>
					<h4>You are about to rent:</h4>
					<ul>
						<li>Game Title: <em>{{ book.title }}</em></li>
						<li>Price: <em>${{ book.price }}</em></li>
					</ul>
				</div>

				<div>
					<h4>Use this for testing:</h4>
					<ul>
						<li>Card Number: 424242424242</li>
						<li>CVC Code: 3-digit CVC</li>
						<li>Expiration: MM/YY</li>
					</ul>
				</div>
			</section>

			<section>
				<h3>One time payment</h3>
				<form action="#">
					<div class="form-group">
						<label for="cc-number">Credit Card Info</label>
						<input type="text"
									 class="form-control"
									 name="cc-number"
									 id="cc-number"
									 placeholder="XXXXXXXXXXXXXXXX"
									 v-model="card.number"
									 required>
					</div>

					<div class="form-group">
						<label for="cvc-number">CVC</label>
						<input type="text"
									 class="form-control"
									 name="cvc-number"
									 id="cvc-number"
									 placeholder="CVC"
									 v-model="card.cvc"
									 required>
					</div>

					<div class="form-group">
						<label for="expiration">Card Expiration Date</label>
						<input type="text"
									 class="form-control"
									 name="expiration"
									 id="expiration"
									 placeholder="MM/YY"
									 v-model="card.exp"
									 required>
					</div>
					<button class="button submit" @click.prevent="validate" :disabled="stripeCheck">Submit</button>
				</form>
				<div v-show="errors">
					<ol class="text-danger">
						<li v-for="(error, index) in errors" :key="index">
							{{ error }}
						</li>
					</ol>
				</div>
			</section>
		</article>
	</section>
</template>

<script>
import axios from 'axios';

export default {
	data() {
		return {
			book: {
				title: '',
				publisher: '',
				instock: [],
				price: '',
			},
			card: {
				number: '',
				cvc: '',
				exp: '',
			},
			errors: [],
			stripePublishableKey: 'pk_test_2R90IX5GB273e9m9PSL40sgu00JA9PyQB4',
			stripeCheck: false,
		};
	},
	methods: {
		getBook() {
			const path = `http://localhost:5000/books/${this.$route.params.id}`;
			axios.get(path)
				.then((res) => {
					this.book = res.data.book;
				})
				.catch((error) => {
				// eslint-disable-next-line
				console.error(error);
				});
		},
		validate() {
			this.errors = [];
			let valid = true;
			if (!this.card.number) {
				valid = false;
				this.errors.push('Card number is required');
			}
			if (!this.card.cvc) {
				valid = false;
				this.errors.push('CVC is required');
			}
			if (!this.card.exp) {
				valid = false;
				this.errors.push('Expiration date is required');
			}
			if (valid) {
				this.createToken();
			}
		},
		createToken() {
			this.stripeCheck = true;
			window.Stripe.setPublishableKey(this.stripePublishableKey);
			window.Stripe.createToken(this.card, (status, response) => {
				if (response.error) {
					this.stripeCheck = false;
					this.errors.push(response.error.message);
					// eslint-disable-next-line
					console.error(response);
				} else {
					const payload = {
						book: this.book,
						token: response.id,
					};
					const path = 'http://localhost:5000/charge';
					axios.post(path, payload)
						.then((res) => {
							this.$router.push({ path: `/complete/${res.data.charge.id}` });
						})
						.catch((error) => {
							// eslint-disable-next-line
							console.error(error);
						});
				}
			});
		},
	},
	created() {
		this.getBook();
	},
};
</script>
