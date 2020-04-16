<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from 'axios';

const GAMESAPI = 'https://games-api-juues4q2ia-uc.a.run.app';

export default {
	name: 'Ping',
	data() {
		return {
			msg: 'Hello!',
		};
	},
	methods: {
		getMessage() {
			const path = `${GAMESAPI}/ping`;
			axios
				.get(path)
				.then((res) => {
					this.msg = res.data;
				})
				.catch((error) => {
					// eslint-disable-next-line
          console.error(error);
				});
		},
	},
	created() {
		this.getMessage();
	},
};
</script>
