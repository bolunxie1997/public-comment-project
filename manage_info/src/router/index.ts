import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Profile from '../components/Profile.vue'
import Comments from '../components/Comments.vue'
import  Replies from '../components/Replies.vue'
import Shops from '../components/Shops.vue'
import Users from '../components/Users.vue'


const routes: Array<RouteRecordRaw> = [
  {
    path:"/profile",
    name:'Profile',
    component:Profile
  },
  {
    path: '/comments',
    name: 'Comments',
    component: Comments
  },
  {
    path:"/replies",
    name:"Replies",
    component:Replies
  },
  {
    path: '/shops',
    name: 'Shops',
    component: Shops
  },
  {
    path: '/users',
    name: 'Users',
    component: Users
  },
  {
    path:"/",
    redirect:"/profile",
  }
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router