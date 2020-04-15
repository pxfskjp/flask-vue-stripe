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
  #app {
   margin: 0 auto;
   min-height: 100vh; /* will cover the 100% of viewport */
   overflow: hidden;
   display: block;
   position: relative;
   padding-bottom: 100px; /* height of your footer */
   font-family: ;
   text-align: center;
   min-width: 60px;
  }

  h1 {
  margin-top: 4rem;
  }
</style>
