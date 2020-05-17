import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import About from '@/components/About'
import Daily from '@/components/Daily'
import Work from '@/components/Work'
import Essays from '@/components/Essays'
import EssayDetails from '@/components/EssayDetails'
import ProjectDetails from '@/components/ProjectDetails'

Vue.use(Router)

export default new Router({
  mode: 'history',
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
      meta: {
        showModal: false
      },
      component: Work
    },
    {
      path: '/work/:projectid',
      name: 'project',
      meta: {
        showModal: true
      },
      props: true,
      component: ProjectDetails
    },
    {
      path: '/essays',
      name: 'Essays',
      component: Essays
    },
    {
      path: '/essays/:eid',
      name: 'essaydetail',
      props: true,
      component: EssayDetails
    },
  ]
})
