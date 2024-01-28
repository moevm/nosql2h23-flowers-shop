<template>
    <Navbar />
    <div class="app">
        <router-view></router-view>
    </div>
    <Footer />
</template>

<script setup>
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'

onMounted(() => {
    store.loadData();
    store.loadStorage();
})
</script>

<style scoped>
.app {
    min-height: 70vh;
}
</style>
