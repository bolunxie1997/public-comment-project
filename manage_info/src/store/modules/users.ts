import axios from 'axios'
import config from '../../config'
import { notification } from 'ant-design-vue';
import { UserItem } from '@/Interfaces';


const state = () => ({
    users: null
})

const getters = {

}

const actions = {
    async getUsers({ state }:any) {
        axios.get(config.serverURL+'/getusers/',{
            withCredentials:true
        }).then(response=>{
            if(response.data['result']== -1){
                notification.warning({
                    message:'Get User List failed',
                    description:response.data['msg']
                });
            }
            else{
                state.users = response.data['users'];
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