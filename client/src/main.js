import BootstrapVue from 'bootstrap-vue';
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import vuetify from './plugins/vuetify';

Vue.use(BootstrapVue);

Vue.config.productionTip = false;

new Vue({
	router,
	vuetify,
	render: (h) => h(App),
}).$mount('#app');
