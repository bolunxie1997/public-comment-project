<template>
    <div class="clearfix">
        <a-upload
            v-model:file-list="fileList"
            list-type="picture-card"
            @preview="handlePreview"
            :before-upload="beforeUpload"
            @change="handleChange"
        >
            <div v-if="fileList.length < 1">
                <plus-outlined />
                <div class="ant-upload-text">Upload</div>
            </div>
        </a-upload>
        <a-modal :visible="previewVisible" :footer="null" @cancel="handleCancel">
            <img alt="example" style="width: 100%" :src="previewImage" />
        </a-modal>
    </div>
    
</template>
<script lang="ts">
import { PlusOutlined } from '@ant-design/icons-vue';
import { defineComponent, ref, Ref } from 'vue';
import { FileInfo, FileItem } from '@/Interfaces';


function getBase64(file: File) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => resolve(reader.result);
        reader.onerror = error => reject(error);
    });
}



export default defineComponent({
    components: {
        PlusOutlined,
    },
    emits:["avatarChange"],
    setup(props,context) {
        const previewVisible = ref<boolean>(false);
        const previewImage = ref<string | undefined>('');
        

        const fileList = ref<FileItem[]>([

        ]);
        const handleCancel = () => {
            previewVisible.value = false;
        };
        const handlePreview = async (file: FileItem) => {
            if (!file.url && !file.preview) {
                file.preview = (await getBase64(file.originFileObj)) as string;
            }
            previewImage.value = file.url || file.preview;
            previewVisible.value = true;
        };
        const handleChange = ({ fileList: newFileList }: FileInfo) => {
            if(newFileList.length>0)
                context.emit("avatarChange",newFileList);
        };

        

        const beforeUpload = () => {
            console.log(fileList.value)
            return false;
        };
        
        const resetImgList = ()=>{
            fileList.value = [];

        }

        return {
            previewVisible,
            previewImage,
            fileList,
            handleCancel,
            handlePreview,
            handleChange,
            beforeUpload,
            resetImgList
        };
    },
});
</script>
<style>
/* you can make up upload button and sample style by using stylesheets */
.ant-upload-select-picture-card i {
    font-size: 32px;
    color: #999;
}

.ant-upload-select-picture-card .ant-upload-text {
    margin-top: 8px;
    color: #666;
}
</style>
