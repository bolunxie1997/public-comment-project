<template>
  <a-layout>
    <a-layout-sider v-model:collapsed="collapsed" :trigger="null" collapsible id="sideBar">
      <div class="logo" />
      <a-menu v-model:selectedKeys="selectedKeys" theme="dark" mode="inline">
        <a-menu-item key="1">
          <router-link to="profile">
            <profile-outlined />
            <span>Edit Profile</span>
          </router-link>
        </a-menu-item>
        <a-menu-item key="2">
          <router-link to="comments">
            <comment-outlined />
            <span>Manage Comments</span>
          </router-link>
        </a-menu-item>
        <a-menu-item key="3">
          <router-link to="replies">
            <message-outlined />
            <span>Manage Replies</span>
          </router-link>
        </a-menu-item>

        <a-menu-item key="4">
          <router-link to="shops">
            <shop-outlined />
            <span>Manage Shops</span>
          </router-link>
        </a-menu-item>

        <a-menu-item key="5">
          <router-link to="users">
            <user-outlined/>
            <span>Manage Users</span>
          </router-link>
        </a-menu-item>
      </a-menu>
    </a-layout-sider>
    <a-layout>
      <a-layout-header style="background: #fff; padding: 0">
        <menu-unfold-outlined
          v-if="collapsed"
          class="trigger"
          @click="() => (collapsed = !collapsed)"
        />
        <menu-fold-outlined v-else class="trigger" @click="() => (collapsed = !collapsed)" />
      </a-layout-header>
      <a-layout-content
        :style="{ margin: '24px 16px', padding: '24px', background: '#fff', minHeight: '280px' }"
      >
        <router-view/>
      </a-layout-content>
    </a-layout>
  </a-layout>
</template>
<script lang="ts">
import {
  UserOutlined,
  CommentOutlined,
  MessageOutlined,
  ShopOutlined,
  ProfileOutlined,
  MenuUnfoldOutlined,
  MenuFoldOutlined,
} from '@ant-design/icons-vue';
import { defineComponent, ref } from 'vue';
export default defineComponent({
  components: {
    UserOutlined,
    CommentOutlined,
    MessageOutlined,
    ShopOutlined,
    ProfileOutlined,
    MenuUnfoldOutlined,
    MenuFoldOutlined,
  },
  setup() {
    return {
      selectedKeys: ref<string[]>(['1']),
      collapsed: ref<boolean>(false),
    };
  },
});
</script>
<style>
#sideBar {
  height: 100vh;
}

.trigger {
  font-size: 18px;
  line-height: 64px;
  padding: 0 24px;
  cursor: pointer;
  transition: color 0.3s;
}

.trigger:hover {
  color: #1890ff;
}

.logo {
  height: 32px;
  background: rgba(255, 255, 255, 0.3);
  margin: 16px;
}

.site-layout .site-layout-background {
  background: #fff;
}
</style>
