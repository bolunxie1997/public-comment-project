<template>
  <a-table bordered :data-source="dataSource" :columns="columns">
    <template #bodyCell="{ column, record }">
      <template v-if="column.dataIndex === 'operation'">
        <a-popconfirm
          v-if="dataSource.length && record.state == 1"
          title="Sure to delete?"
          @confirm="onDelete(record.id)"
        >
          <a-button type="link" danger>Delete</a-button>
        </a-popconfirm>

        <a-popconfirm
          v-if="dataSource.length && record.state == 0"
          title="Sure to recover?"
          @confirm="onRecover(record.id)"
        >
          <a-button type="link" success>Recover</a-button>
        </a-popconfirm>
      </template>
      <template v-else-if="column.dataIndex === 'type'">
        <a-tag color="red" v-if="record.type == 2">Admin</a-tag>
        <a-tag color="blue" v-else-if="record.type == 1">Merchant</a-tag>
        <a-tag color="green" v-else-if="record.type == 0">User</a-tag>
      </template>
      <template v-else-if="column.dataIndex === 'gender'">
        <a-tag color="cyan" v-if="record.gender == 'Male'">{{ record.gender }}</a-tag>
        <a-tag color="pink" v-else-if="record.gender == 'Female'">{{ record.gender }}</a-tag>
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
  </a-table>
</template>
<script lang="ts">
import { computed, defineComponent, reactive, ref } from 'vue';
import type { Ref, UnwrapRef } from 'vue';
import { UserItem } from '@/Interfaces';
import { useStore } from 'vuex';
import {CloseCircleOutlined,CheckCircleOutlined } from '@ant-design/icons-vue';

export default defineComponent({
  components:{
    CloseCircleOutlined,
    CheckCircleOutlined
  },
  setup(props, context) {
    const store = useStore()
    store.dispatch("getUsers");

    const columns = [
      {
        title: 'username',
        dataIndex: 'username',
        width: '30%',
      },
      {
        title: 'age',
        dataIndex: 'age',
        sorter: (a: UserItem, b: UserItem) => a.age - b.age,
      },
      {
        title: 'gender',
        dataIndex: 'gender',

      },
      {
        title: 'type',
        dataIndex: 'type',
        filters: [
          {
            text: 'Admin',
            value: 2
          },
          {
            text: 'Merchant',
            value: 1
          },
          {
            text: 'user',
            value: 0
          }
        ],
        onFilter: (value: number | string, record: UserItem) => record.type == value
      },
      {
        title: 'state',
        dataIndex: 'state',
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


    const dataSource: Ref<UserItem[]> = computed((): UserItem[] => {
      console.log(store.state.users)
      return store.state.users.users
    })
    const count = computed(() => dataSource.value.length + 1);


    const onDelete = (key: string | number) => {
      // dataSource.value = dataSource.value.filter(item => item.id !== key);
      store.dispatch("deleteUserById", key);
    };
    const onRecover = (key:string | number) => {
      store.dispatch("recoerUserById", key);
    }


    return {
      columns,
      onDelete,
      onRecover,
      dataSource,
      count,

    };
  },
});
</script>
<style>
</style>
