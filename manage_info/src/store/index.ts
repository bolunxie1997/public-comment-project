import { createStore } from 'vuex'
import users from './modules/users'
import replies from './modules/replies'
import comments from './modules/comments'
import shops from './modules/shops'
import axios from 'axios'
import config from '@/config'
import { notification } from 'ant-design-vue'

export default createStore({
  state: () => ({
    shopTypes: []
  }),
  getters: {
    getShopTypes(state:any){
      return state.shopTypes.map((type:any)=>({
        text:type.name,
        value:type.name
      }))
    }
  },
  actions: {
    getShopTypes({ state }: any) {
      if (state.shopTypes.length > 0)
        return;
      return axios.get(config.serverURL + '/shoptypes/', {
        withCredentials: true
      }).then(response => {
        if (response.data['result'] == -1) {
          notification.warning({
            message: 'Get Shop Types failed',
            description: response.data['msg']
          });
        }
        else {
          console.log('get shop types finish');
          state.shopTypes = response.data;
        }
      });
    }
  },
  modules: {
    users,
    replies,
    comments,
    shops
  }
})
