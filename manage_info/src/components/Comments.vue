<template>
  <a-table bordered :data-source="dataSource" :columns="columns" :row-key="'id'">
    
    <template #bodyCell="{ column, record }">
      <template v-if="column.dataIndex === 'operation'">
        <a-popconfirm
          v-if="dataSource.length && record.state == 1"
          title="Sure to delete?"
          @confirm.prevent="onDelete(record.id)"
        >
          <a-button type="link" danger>Delete</a-button>
        </a-popconfirm>

        <a-popconfirm
          v-if="dataSource.length && record.state == 0"
          title="Sure to recover?"
          @confirm.prevent="onRecover(record.id)"
        >
          <a-button type="link" success>Recover</a-button>
        </a-popconfirm>
      </template>
      <template v-else-if="column.dataIndex === 'shop_type'">{{ record.shop.type }}</template>
      <template v-else-if="column.dataIndex === 'shop_name'">{{ record.shop.name }}</template>
      <template v-else-if="column.dataIndex === 'rating'">
        <a-rate :value="record.rating" disabled />
      </template>
      <template v-else-if="column.dataIndex === 'state'">
        <a-tag color="error" v-if="record.state == 0">
          <template #icon>
            <close-circle-outlined />
          </template>
          Deleted
        </a-tag>
        <a-tag color="success" v-else>
          <template #icon>
            <check-circle-outlined />
          </template>
          Active
        </a-tag>
      </template>
      <template v-else-if="column.dataIndex === 'ctime'">{{ record.ctime.split(".")[0] }}</template>
    </template>
    <template #expandedRowRender="{ record }">
      <img :src="serverURL + '/' + record.author.avatar" class="user-avatar" />
      <div style="margin-left: 80px;">
        <h3>{{ record.author.username }}</h3>
        <p>{{ record.content }}</p>
        <div>
          <a-image v-for="(img,index) in record.imgs" :key="index" :src="serverURL + '/' + img" ></a-image>
        </div>
      </div>
    </template>
  </a-table>
</template>

<script lang="ts">
import { computed, defineComponent, reactive, ref } from 'vue';
import type { Ref, UnwrapRef } from 'vue';
import { CommentItem } from '@/Interfaces';
import { useStore } from 'vuex';
import { CloseCircleOutlined, CheckCircleOutlined } from '@ant-design/icons-vue';
import config from '@/config';

export default defineComponent({
  components: {
    CloseCircleOutlined,
    CheckCircleOutlined
  },
  setup(props, context) {
    const store = useStore()
    store.dispatch("getComments");
    const serverURL = ref(config.serverURL);
    const shopTypesFilters = computed(() => store.getters.getShopTypes);
  
    
    const columns = [
      {
        title: 'ID',
        dataIndex: 'id',
      },
      {
        title: 'Rating',
        dataIndex: 'rating',
        sorter: (a: CommentItem, b: CommentItem) => a.rating - b.rating,
      },
      {
        title: 'Shop Name',
        dataIndex: 'shop_name',
      },
      {
        title: 'Shop Type',
        dataIndex: 'shop_type',
        filters: shopTypesFilters.value,
        onFilter: (value: number | string, record: CommentItem) => record.shop.type == value
      },
      // {
      //   title: 'Author Name',
      //   dataIndex: 'author_name',
      // },
      {
        title: 'state',
        dataIndex: 'state',
        filters:[
          {
            text:"Deleted",
            value:0
          },
          {
            text:"Active",
            value:1
          }
        ],
        onFilter: (value: number | string, record: CommentItem) => record.state == value

      },
      {
        title: 'create time',
        dataIndex: 'ctime',
      },
      {
        title: 'operation',
        dataIndex: 'operation',
      },
    ];


    const dataSource: Ref<CommentItem[]> = computed((): CommentItem[] => {
      
      return store.state.comments.comments
    })

    const onDelete = (key: string | number) => {
      // dataSource.value = dataSource.value.filter(item => item.id !== key);
      store.dispatch("deleteCommentById", key);
    };
    const onRecover = (key: string | number) => {
      store.dispatch("recoerCommentById", key);
    }


    return {
      columns,
      onDelete,
      onRecover,
      dataSource,
      serverURL
    };
  },
});
</script>
<style>
.user-avatar {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  float: left;
}
.ant-image{
  cursor: pointer;
  margin-right: 10px;
  width: 200px;
}
</style>
