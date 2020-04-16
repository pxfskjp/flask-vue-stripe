<template>
  <div id="app">
		<Navigation></Navigation>
    <router-view/>
		<Footer></Footer>
  </div>
</template>

<script>
import Navigation from './components/Navigation.vue';
import Footer from './components/Footer.vue';

export default {
	name: 'app',
	components: {
		Navigation,
		Footer,
	},
	  watch: {
		$route(to) {
			document.title = to.meta.title || 'The Sentry Box';
		},
	},
};


</script>

<style>
	:root {
		--lahmian-medium: rgba(238, 238, 226, 1);
		--spiritstone-red: rgba(239,85,44, 1);
		--averland-sunset: rgba(247,189,52, 1);
	}

	body {
		background-color: darkslategray;
	}

  #app {
	 font-family: Avenir, Helvetica, Arial, sans-serif;
	 -webkit-font-smoothing: antialiased;
   -moz-osx-font-smoothing: grayscale;
	 margin: 0 auto;
	 color: #2c3e50;
   min-height: 100vh; /* will cover the 100% of viewport */
   overflow: hidden;
   display: block;
   position: relative;
   padding-bottom: 100px; /* height of your footer */
   text-align: center;
   min-width: 60px;
  }
  h1 {
  margin-top: 4rem;
	}

</style>
