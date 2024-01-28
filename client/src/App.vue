<template>
    <Navbar />
    <div class="app">
        <router-view></router-view>
    </div>
    <Footer />
</template>

<script setup>
import { onMounted } from 'vue';
import { useFlowersStore } from './store/index';
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'

const store = useFlowersStore();

onMounted(() => {
    store.loadData();
    store.loadStorage();
    store.getCart()
})
</script>

<style scoped>
.app {
    min-height: 70vh;
}
</style>
