<template>
  <a-table bordered :data-source="dataSource" :columns="columns">
    <template #bodyCell="{ column, record }">
      
      <template v-if="column.dataIndex === 'operation'">
        <a-popconfirm
          v-if="dataSource.length"
          title="Sure to delete?"
          @confirm="onDelete(record.id)"
        >
          <a-button type="link" danger>Delete</a-button>
        </a-popconfirm>
      </template>
    </template>
  </a-table>
</template>
<script lang="ts">
import { computed, defineComponent, reactive, ref } from 'vue';
import type { Ref, UnwrapRef } from 'vue';
import { UserItem } from '@/Interfaces';
import { useStore } from 'vuex';


export default defineComponent({
  setup(props,context) {
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
      },
      {
        title: 'gender',
        dataIndex: 'gender',
      },
      {
        title: 'type',
        dataIndex: 'type',
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
    
    
    const dataSource: Ref<UserItem[]> = computed(()=>store.state.users.length>0 ? store.state.users : [])
    const count = computed(() => dataSource.value.length + 1);
    

    const onDelete = (key: string) => {
      dataSource.value = dataSource.value.filter(item => item.id !== key);
    };
    

    return {
      columns,
      onDelete,
      dataSource,
      count,
      
    };
  },
});
</script>
<style>

</style>
