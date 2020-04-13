<template>
	<article class="order-complete">
		<div>
			<h1>Thanks for renting {{ this.book }}</h1>
			<router-link to="/" class="button return">Back</router-link>
		</div>
	</article>
</template>

<script>
import axios from 'axios';

export default {
	data() {
		return {
			book: '',
		};
	},
	methods: {
		getChargeInfo() {
			const path = `http://localhost:5000/charge/${this.$route.params.id}`;
			axios.get(path)
				.then((response) => {
					this.book = response.data.charge.description;
				})
				.catch((error) => {
					// eslint-disable-next-line
					console.error(error);
				});
		},
	},
	created() {
		this.getChargeInfo();
	},
};
</script>
