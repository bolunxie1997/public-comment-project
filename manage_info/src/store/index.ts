import { createStore } from 'vuex'
import users from './modules/users'
import replies from './modules/replies'
import comments from './modules/comments'

export default createStore({
  
  modules: {
    users,
    replies,
    comments
  }
})
