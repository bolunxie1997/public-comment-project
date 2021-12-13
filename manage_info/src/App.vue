<template>
  <a-layout>
    <a-layout-sider v-model:collapsed="collapsed" :trigger="null" collapsible id="sideBar">
      <div class="logo">
      </div>
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
            <user-outlined />
            <span>Manage Users</span>
          </router-link>
        </a-menu-item>
      </a-menu>
    </a-layout-sider>
    <a-layout style="height: 100vh;overflow: auto;">
      <a-layout-header style="background: #fff; padding: 0" class="nav-header">
        <menu-unfold-outlined
          v-if="collapsed"
          class="trigger"
          @click="() => (collapsed = !collapsed)"
        />
        <menu-fold-outlined v-else class="trigger" @click="() => (collapsed = !collapsed)" />
        <div style="display: inline-block;position: absolute;right: 20px;">
          <div style="display: flex;">
            <div>
              <img style="width: 40px;height: 40px; border-radius: 50%  ;" v-if="user!=null" :src="user.avatar"  />
            </div>
            <h3 style="margin-left: 20px;" v-if="user == null">
              <a href="http://127.0.0.1:5500/login.html">Login</a>
            </h3>
            <h3 style="margin-left: 20px;" v-if="user!=null">{{ user.username }}</h3>
          </div>
        </div>
      </a-layout-header>
      <a-layout-content
        :style="{ margin: '24px 16px', padding: '24px', background: '#fff', minHeight: '280px' }"
      >
        <router-view />
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
import { computed, defineComponent, ref } from 'vue';
import { useStore } from 'vuex';
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
    const store = useStore();
    //global state
    store.dispatch("getUser")
    store.dispatch("getShopTypes")
    const user = computed(()=>store.state.users.user);
    return {
      user,
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
  height: 50px;
  background-size: 170px 50px;
  /* background: rgba(255, 255, 255, 0.3); */
  background-image:url("./assets/logo.png");
  text-align: center;
  margin: 16px;
}



.site-layout .site-layout-background {
  background: #fff;
}

.nav-header{
    display: flex;
    justify-content: space-between;
    align-items: center;
}
</style>
