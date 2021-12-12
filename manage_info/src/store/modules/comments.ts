import axios from 'axios'
import config from '../../config'
import { notification } from 'ant-design-vue';


const state = () => ({
    comments: null
})

const getters = {

}

const actions = {
    async getComments({ state }:any) {
        axios.get(config.serverURL+'/getcomments/',{
            withCredentials:true
        }).then(response=>{
            if(response.data['result']== -1){
                notification.warning({
                    message:'Get User List failed',
                    description:response.data['msg']
                });
            }
            else{
                state.comments = response.data['comments'];
            }
        })
    }

}

const mutations = {
    
}

export default {
    state,
    getters,
    mutations,
    actions
}