<template>
    <div className="addProduct">
        <input 
            className="addProduct__image inputStyled" 
            type="file" 
            name="photo" 
            placeholder="изображение товара"
            multiple accept="image/*,image/jpeg"
        >

        <input 
            className="addProduct__name inputStyled" 
            placeholder="Наименование букета"
            v-model="name"
        >

        <input 
            className="addProduct__price inputStyled"
            type="number"
            placeholder="Цена"
            v-model="price"
        >

        <input 
            className="addProduct__date inputStyled"
            type="date"
            placeholder="Срок годности"
            v-model="date"
        >

        <textarea
            class="addProduct__description inputStyled" 
            placeholder="Описание товара" 
            v-model="description" 
        />

        <button className="app_button">
            Добавить
        </button>

    </div>
</template>


<script setup>
import { ref } from 'vue';

const name = ref('');
const price = ref();
const date = ref();
const description = ref('');

</script>

<style lang="scss" scoped>
.addProduct {
    border-radius: 15px;
    background: var(--color-white);
    padding: 50px;

    display: flex;
    flex-direction: column;
    gap: 20px;

    &__image,
    &__name {
        width: 517px;
    }

    &__price,
    &__date {
        width: 200px;
    }

    &__description {
        width: 517px;
        height: 100px;
    }
}
</style>