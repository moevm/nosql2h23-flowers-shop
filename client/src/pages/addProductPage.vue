<template>
    <div className="addProductPage">
        <h2 className="section_title">
            Добавление товара
        </h2>
        
        <addProduct />
    </div>
</template>

<script setup>
import { ref } from 'vue';
import addProduct from '../components/addProduct.vue';

</script>

<style lang="scss" scoped>
.addProductPage {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 50px;
}
</style>