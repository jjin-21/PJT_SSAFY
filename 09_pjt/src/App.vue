<script setup>
import { RouterView, RouterLink } from 'vue-router';
const back = function() {
  window.history.back()
}

</script>



<template>
  <div>
    <header>
      <nav>
        <a href=""><strong>MyTube</strong></a>
        <RouterLink :to="{name:'home'}">Home</RouterLink>
        <RouterLink :to="{name:'search'}">Search</RouterLink>
        <RouterLink :to="{name:'later'}">Later</RouterLink>
      </nav>
    </header>

    <main class="container">
      <a href="" class="back" @click.prevent="back">뒤로가기</a>
      <RouterView />
    </main>
  </div>
</template>


<style scoped>
header {
  background-color: rgb(65, 64, 64);
  height: 40px;
  display: flex;
  align-items: center;
  margin-bottom: 15px;
}

nav > a, RouterLink {
  color: white;
  text-decoration: none; /* 하이퍼링크 밑줄 제거 */
  margin-left: 15px;
}

main > a {
  text-decoration: none; /* 하이퍼링크 밑줄 제거 */
  color: black;
}
</style>