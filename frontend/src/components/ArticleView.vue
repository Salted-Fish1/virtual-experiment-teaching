<template>
  <div v-for="article in info" :key="article.url" id="articles">
    <h2>
      {{ article.title }}
    </h2>
    <p>
      {{ article.body }}
    </p>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { ref } from 'vue'
import axios from 'axios'
export default defineComponent({
  setup() {
    let info: any = ref('')

    axios.get('/api/article').then((response) => {
      info.value = response.data
      console.log(info)
    })

    return {
      info
    }
  }
})
</script>

<style scoped></style>
