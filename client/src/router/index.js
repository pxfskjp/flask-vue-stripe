
import Vue from 'vue';
import Router from 'vue-router';
import Books from '../components/Books.vue';
import Order from '../components/Order.vue';
import OrderComplete from '../components/OrderComplete.vue';
import Home from '../components/Home.vue';
import About from '../components/About.vue';
import FAQ from '../components/FAQ.vue';
import Events from '../components/Events.vue';


Vue.use(Router);

export default new Router({
	mode: 'history',
	base: process.env.BASE_URL,
	routes: [
		{
			path: '/books',
			name: 'Books',
			component: Books,
		},
		{
			path: '/order/:id',
			name: 'Order',
			component: Order,
		},
		{
			path: '/complete/:id',
			name: 'OrderComplete',
			component: OrderComplete,
		},
		{
			path: '/',
			name: 'Home',
			component: Home,
		},
		{
			path: '/FAQ',
			name: 'FAQ',
			component: FAQ,
		},
		{
			path: '/about',
			name: 'About',
			component: About,
		},
		{
			path: '/events',
			name: 'Events',
			component: Events,
		},
	],
});
