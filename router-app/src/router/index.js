import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import About from '@/components/About'
import Daily from '@/components/Daily'
import Work from '@/components/Work'
import Essays from '@/components/Essays'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/about',
      name: 'About',
      component: About
    },
    {
      path: '/daily',
      name: 'Daily',
      component: Daily
    },
    {
      path: '/work',
      name: 'Work',
      component: Work
    },
    {
      path: '/essays',
      name: 'Essays',
      component: Essays
    }
  ]
})
