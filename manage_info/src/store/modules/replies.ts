import axios from 'axios'
import config from '../../config'
import { notification } from 'ant-design-vue';


const state = () => ({
    replies: null
})

const getters = {

}

const actions = {
    async getReplies({ state }:any) {
        axios.get(config.serverURL + '/getreplies/',{
            withCredentials:true
        }).then(response=>{
            if(response.data['result']== -1){
                notification.warning({
                    message:'Get User List failed',
                    description:response.data['msg']
                });
            }
            else{
                state.replies = response.data['replies'];
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