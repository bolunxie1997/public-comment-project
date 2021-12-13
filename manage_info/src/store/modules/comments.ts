import axios from 'axios'
import config from '../../config'
import { notification } from 'ant-design-vue';
import { CommentItem } from '@/Interfaces';



const state = () => ({
    comments: [],
})

const getters = {
    
}

const actions = {
    async getComments({ state,dispatch }:any) {
        dispatch('getShopTypes',null,{root:true});
        axios.get(config.serverURL+'/getcomments/',{
            withCredentials:true
        }).then(response=>{
            if(response.data['result']== -1){
                notification.warning({
                    message:'Get Comment List failed',
                    description:response.data['msg']
                });
            }
            else{
                state.comments = response.data['comments'];
            }
        });
        
    },
    async deleteCommentById({ state ,rootGetters }:any,comment_id:any) {
        axios.get(config.serverURL + '/deletecomment/'+comment_id,{
            withCredentials:true
        }).then(response=>{
            if(response.data['result']== -1){
                notification.warning({
                    message:'Delete Comment failed',
                    description:response.data['msg']
                });
            }
            else{
                if(rootGetters.isManager)
                    state.comments.find((item:CommentItem)=>item.id == comment_id).state = 0;
                else
                    state.comments = state.comments.filter((item:CommentItem)=>item.id!=comment_id)

            }
        })
    },
    async recoerCommentById({ state }:any,comment_id:any) {
        axios.get(config.serverURL + '/recovercomment/'+comment_id,{
            withCredentials:true
        }).then(response=>{
            if(response.data['result']== -1){
                notification.warning({
                    message:'Recover Comment failed',
                    description:response.data['msg']
                });
            }
            else{
                // state.comments = state.comments.filter((item:CommentItem)=>item.id!=comment_id)
                state.comments.find((item:CommentItem)=>item.id == comment_id).state = 1;
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