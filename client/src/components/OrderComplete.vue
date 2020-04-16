<template>
	<article class="order-complete">
		<div>
			<h1>Thanks for renting {{ this.book }}</h1>
			<router-link to="/books" class="button return">Back</router-link>
		</div>
	</article>
</template>

<script>
import axios from 'axios';

const GAMESAPI = 'https://games-api-juues4q2ia-uc.a.run.app';

export default {
	data() {
		return {
			book: '',
		};
	},
	methods: {
		getChargeInfo() {
			const path = `${GAMESAPI}/charge/${this.$route.params.id}`;
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
