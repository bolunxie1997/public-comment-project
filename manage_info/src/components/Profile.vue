<template >
    <h2 style="text-align: right;">Edit Profile</h2>
    <a-form
        ref="formRef"
        :model="formState"
        :rules="rules"
        v-bind="layout"
    >
        <a-form-item  has-feedback label="UserName" name="username" 
        :rules="{ required: true, message: 'Please input the username', trigger:'change'}">
            <a-input v-model:value="formState.username" type="text">
                <template #prefix>
                    <UserOutlined style="color: rgba(0, 0, 0, 0.25)" />
                </template>
            </a-input>
        </a-form-item>

        <a-form-item has-feedback label="Password" name="pass">
            <a-input v-model:value="formState.pass" type="password" autocomplete="off" >
                <template #prefix>
                    <LockOutlined style="color: rgba(0, 0, 0, 0.25)" />
                </template>
            </a-input>
        </a-form-item>

        <a-form-item has-feedback label="Confirm" name="checkPass">
            <a-input v-model:value="formState.checkPass" type="password" autocomplete="off" >
                <template #prefix>
                    <LockOutlined style="color: rgba(0, 0, 0, 0.25)" />
                </template>
            </a-input>
        </a-form-item>
        <a-form-item has-feedback label="Age" name="age">
            <a-input-number v-model:value="formState.age" />
        </a-form-item>
        <a-form-item label="Avatar" name="avatar">
            <UserAvatar @avatar-change="changAvatar($event)" ref="userAvatarRef"></UserAvatar>
        </a-form-item>
        <a-form-item :wrapper-col="{ span: 14, offset: 4 }">
            <a-button type="primary" html-type="submit" @click.prevent='submitForm'>Submit</a-button>
            <a-button style="margin-left: 10px" @click="resetForm">Reset</a-button>
        </a-form-item>
    </a-form>
</template>
<script lang="ts">
import type { RuleObject } from 'ant-design-vue/es/form';
import { defineComponent, reactive, ref } from 'vue';
import type { UnwrapRef } from 'vue';
import UserAvatar from "./Avatar.vue"
import { FileItem, FormState } from '@/Interfaces';
import { UserOutlined, LockOutlined } from '@ant-design/icons-vue';

export default defineComponent({
    components: {
        UserAvatar,
        UserOutlined,
        LockOutlined
    },
    setup() {
        const formRef = ref();
        const userAvatarRef = ref();
        const formState: UnwrapRef<FormState> = reactive({
            pass: '',
            checkPass: '',
            username: '',
            age: undefined,
        });
        let checkAge = async (_rule: RuleObject, value: number) => {
            if (!value) {
                return Promise.reject('Please input the age');
            }
            if (!Number.isInteger(value)) {
                return Promise.reject('Please input digits');
            } else {
                if (value < 18) {
                    return Promise.reject('Age must be greater than 18');
                } else {
                    return Promise.resolve();
                }
            }
        };
        let validatePass = async (_rule: RuleObject, value: string) => {
            if (value === '') {
                return Promise.reject('Please input the password');
            } else {
                if (formState.checkPass !== '') {
                    formRef.value.validateFields('checkPass');
                }
                return Promise.resolve();
            }
        };
        let validatePass2 = async (_rule: RuleObject, value: string) => {
            if (value === '') {
                return Promise.reject('Please input the password again');
            } else if (value !== formState.pass) {
                return Promise.reject("Two inputs don't match!");
            } else {
                return Promise.resolve();
            }
        };

        var avatar: FileItem;
        const changAvatar = ($event: FileItem[]) => {
            avatar = $event[0];
            console.log(avatar);
        }


        const rules = {
            // username: [{ required: true, validator: checkUser, trigger:'change'}],
            pass: [{ required: true, validator: validatePass, trigger: 'change' }],
            checkPass: [{ required: true, validator: validatePass2, trigger: 'change' }],
            age: [{ validator: checkAge, trigger: 'change' }],
        };
        const layout = {
            labelCol: { span: 4 },
            wrapperCol: { span: 14 },
        };
        
        
        const resetForm = () => {
            formRef.value.resetFields();
        };
        
        const submitForm = ()=>{
            //向后端发送请求
            console.log("submit");
            resetForm();
            console.log(userAvatarRef.value.resetImgList());
            
        }

        return {
            formState,
            formRef,
            rules,
            layout,
            resetForm,
            changAvatar,
            submitForm,
            userAvatarRef
        };
    },
});
</script>

