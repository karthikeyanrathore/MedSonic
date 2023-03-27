<template>
  <div>
    <header class="app-header">
      <app-nav></app-nav>
    </header>
    <router-view></router-view>
  </div>
</template>

<script>
import AppNav from './components/Home'

export default {
  components: {
    AppNav
  }

}
</script>

<style></style>
