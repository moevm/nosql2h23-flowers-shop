<template>
    <div className="addProduct">
        <input 
            className="addProduct__image inputStyled" 
            placeholder="Ссылка на изображение товара"
            v-model="link"
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
            className="addProduct__amount inputStyled"
            type="number"
            placeholder="Количество"
            v-model="amount"
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

        <router-link :to="{ name: 'storage' }">
            <button 
                className="app_button" 
                @click="store.addToStorage({ image: link, name: name, price: price, shelf_life: date, description: description, amount: amount })"
            >
                Добавить
            </button>
        </router-link>
    </div>
</template>


<script setup>
import { ref } from 'vue';
import {useFlowersStore} from '../store/index';

const store = useFlowersStore();

const link = ref('');
const name = ref('');
const price = ref();
const amount = ref();
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
    &__date,
    &__amount {
        width: 200px;
    }

    &__description {
        width: 517px;
        height: 100px;
    }
}
</style>