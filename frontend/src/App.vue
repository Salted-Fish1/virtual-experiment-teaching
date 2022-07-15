<template>
  <ArticleView></ArticleView>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import ArticleView from './components/ArticleView.vue'

export default defineComponent({
  name: 'App',
  components: {
    ArticleView
  }
})
</script>

<style lang="less">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
