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
};

</script>

<style>
  body {
	  font-family: 'Heebo', sans-serif;
  }
  #app {
   margin: 0 auto;
   text-align: center;
   min-width: 60px;
  }
  h1 {
  margin-top: 4rem;
  }
</style>
