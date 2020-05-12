import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import About from '@/components/About'
import Daily from '@/components/Daily'
import Work from '@/components/Work'
import Essays from '@/components/Essays'
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
      children: [
        {
          path: '/work/:projectid',
          name: 'project',
          meta: {
            showModal: true
          },
          props: true,
          component: ProjectDetails
        }
      ],
      meta: {
        showModal: false
      },
      component: Work
    },
    {
      path: '/essays',
      name: 'Essays',
      component: Essays
    }
  ]
})
