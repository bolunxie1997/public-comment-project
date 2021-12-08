import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Home from '../views/Home.vue'
import Profile from '../components/Profile.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path:"/manage/profile",
    name:'Profile',
    component:Profile
  },
  {
    path: '/manage/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/manage/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
