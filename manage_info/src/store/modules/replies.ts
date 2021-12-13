import axios from 'axios'
import config from '../../config'
import { notification } from 'ant-design-vue';
import { ReplyItem } from '@/Interfaces';



const state = () => ({
    replies: [],
})

const getters = {
    
}

const actions = {
    async getReplies({ state,dispatch }:any) {
        axios.get(config.serverURL+'/getreplies/',{
            withCredentials:true
        }).then(response=>{
            if(response.data['result']== -1){
                notification.warning({
                    message:'Get Reply List failed',
                    description:response.data['msg']
                });
            }
            else{
                state.replies = response.data['replies'];
            }
        });
        
    },
    async deleteReplyById({ state , rootGetters  }:any,reply_id:any) {
        axios.get(config.serverURL + '/deletereply/'+reply_id,{
            withCredentials:true
        }).then(response=>{
            if(response.data['result']== -1){
                notification.warning({
                    message:'Delete Reply failed',
                    description:response.data['msg']
                });
            }
            else{
                if(rootGetters.isManager)
                    state.replies.find((item:ReplyItem)=>item.id == reply_id).state = 0;
                else
                    state.replies = state.replies.filter((item:ReplyItem)=>item.id!=reply_id)

            }
        })
    },
    async recoverReplyById({ state }:any,reply_id:any) {
        axios.get(config.serverURL + '/recoverreply/'+reply_id,{
            withCredentials:true
        }).then(response=>{
            if(response.data['result']== -1){
                notification.warning({
                    message:'Recover Reply failed',
                    description:response.data['msg']
                });
            }
            else{
                // state.replies = state.replies.filter((item:ReplyItem)=>item.id!=reply_id)
                state.replies.find((item:ReplyItem)=>item.id == reply_id).state = 1;
            }
        })
    },

}

const mutations = {
    
}

export default {
    state,
    getters,
    mutations,
    actions
}