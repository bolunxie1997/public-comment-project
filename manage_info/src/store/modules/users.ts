import axios from 'axios'
import config from '../../config'
import { notification } from 'ant-design-vue';
import { UserItem } from '@/Interfaces';


const state = () => ({
    users: [],
    msg:"hello?",
    user:null
})

const getters = {

}

const actions = {
    async getUser({state}:any) {
        if(state.user)
            return;
        axios.get(config.serverURL+"/getuser/",{
            withCredentials:true
        }).then(response=>{
            if (response.data['result'] == 0) {
                state.user = response.data;
                state.user.avatar = config.serverURL + '/' + response.data['avatar'] + "?v=" +  Math.random().toString();
            }
        })
    },
    async getUsers({ state }:any) {
        if(state.users.length>0)
            return;
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
    },
    async deleteUserById({ state }:any,user_id:any) {
        axios.get(config.serverURL + '/deleteuser/'+user_id,{
            withCredentials:true
        }).then(response=>{
            if(response.data['result']== -1){
                notification.warning({
                    message:'Delete User failed',
                    description:response.data['msg']
                });
            }
            else{
                // state.users = state.users.filter((item:UserItem)=>item.id!=user_id)
                state.users.find((item:UserItem)=>item.id == user_id).state = 0;
            }
        })
    },
    async recoerUserById({ state }:any,user_id:any) {
        axios.get(config.serverURL + '/recoveruser/'+user_id,{
            withCredentials:true
        }).then(response=>{
            if(response.data['result']== -1){
                notification.warning({
                    message:'Recover User failed',
                    description:response.data['msg']
                });
            }
            else{
                // state.users = state.users.filter((item:UserItem)=>item.id!=user_id)
                state.users.find((item:UserItem)=>item.id == user_id).state = 1;
            }
        })
    },
    


}

const mutations = {
    editUser(state:any,payload:any){
        state.user = payload;
        state.user.avatar = config.serverURL + '/' + payload['avatar'] + "?v=" +  Math.random().toString();

    }
}

export default {
    state,
    getters,
    mutations,
    actions
}