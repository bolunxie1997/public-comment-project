import axios from 'axios'
import config from '../../config'
import { notification } from 'ant-design-vue';
import { ShopItem } from '@/Interfaces';



const state = () => ({
    shops: [],
})

const getters = {
    
}

const actions = {
    async getShops({ state,dispatch }:any) {
        dispatch('getShopTypes',null,{root:true});
        axios.get(config.serverURL+'/getshops/',{
            withCredentials:true
        }).then(response=>{
            if(response.data['result']== -1){
                notification.warning({
                    message:'Get Shop List failed',
                    description:response.data['msg']
                });
            }
            else{
                state.shops = response.data['shops'];
            }
        });
        
    },
    async deleteShopById({ state }:any,shop_id:any) {
        axios.get(config.serverURL + '/deleteshop/'+shop_id,{
            withCredentials:true
        }).then(response=>{
            if(response.data['result']== -1){
                notification.warning({
                    message:'Delete Shop failed',
                    description:response.data['msg']
                });
            }
            else{
                // state.shops = state.shops.filter((item:ShopItem)=>item.id!=shop_id)
                state.shops.find((item:ShopItem)=>item.id == shop_id).state = 0;
            }
        })
    },
    async recoerShopById({ state }:any,shop_id:any) {
        axios.get(config.serverURL + '/recovershop/'+shop_id,{
            withCredentials:true
        }).then(response=>{
            if(response.data['result']== -1){
                notification.warning({
                    message:'Recover Shop failed',
                    description:response.data['msg']
                });
            }
            else{
                // state.shops = state.shops.filter((item:ShopItem)=>item.id!=shop_id)
                state.shops.find((item:ShopItem)=>item.id == shop_id).state = 1;
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