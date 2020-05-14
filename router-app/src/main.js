// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
// Purpose of main is here https://stackoverflow.com/questions/58972232/what-is-the-purpose-of-main-js-app-vue-in-vue-app
import Vue from 'vue'
import App from './App'
import router from './router'
import VueFuse from 'vue-fuse'
import "@/assets/global.css"
import VueMasonry from 'vue-masonry-css'
Vue.use(VueMasonry);
Vue.use(VueFuse);
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
