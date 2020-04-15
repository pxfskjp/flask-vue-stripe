<template>
	<div>
  		<h2></h2>
 		<nav class="navbar">
			<img src="../assets/sboxlogo.png" class="sblogo" alt="sentry box logo">
    		<router-link class="navlinks" v-for="routes in links"
						v-bind:key="routes.id"
						:to="`${routes.page}`">{{routes.text}}</router-link>
			<input type="text" class="search" placeholder="Search...">
  		</nav>
	</div>
</template>


<script>

export default {
	name: 'Navigation',
	data() {
  		return {
    		links: [
      	{
         		id: 0,
         		text: 'Home',
         		page: '/',
				},
				      	{
         		id: 1,
         		text: 'Books',
         		page: '/books',
				},
				      	{
         		id: 2,
         		text: 'FAQ',
         		page: '/faq',
				},
				      	{
         		id: 3,
         		text: 'Events',
         		page: '/events',
				},
				{
         		id: 4,
         		text: 'About',
         		page: '/about',
				},
			],
		};
	},
};
</script>

<style scoped>

	.navbar {
		height: 4rem;
		width: 100%;
		position: fixed;
		left: 0;
		top: 0;
		width: 100%;
		background-color: black;
		display: flex;
		justify-content: space-between;
		align-items: center;
		display: none;
	}

	::placeholder {
		padding-left: 1rem;
	}

	.sblogo {
		width: 15rem;
		height: 5rem;
		overflow: hidden;
	}

	.navlinks {
		color: yellow;
		text-decoration: none;
		justify-content: space-between;
	}

	.search {
		height: 1.5rem;
		width: 9rem;
		border-radius: 20px;
		margin-right: 1rem;
		background-color: white;
	}

</style>
