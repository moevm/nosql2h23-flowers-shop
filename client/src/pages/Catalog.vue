<template>
    <div v-if="flowers" className="catalog">
            <h2 className="section_title">
                Каталог
            </h2>

            <input 
                class="catalog__search inputStyled"
                placeholder="Гортензии"
                v-model="searchValue"
            >

            <div className="catalog__items">
                <div 
                    v-for="flower in searchFlowers()" 
                    :key="flower.id" 
                >
                    <router-link
                        :to="{
                            name: 'flower',
                            path: '/catalog/' + flower.id,
                            params: { id: flower.id }
                        }">
                    >
                        <img 
                            class="catalog__item"
                            :src="flower.image"
                        />
                    </router-link>
                </div>
            </div>
        </div>
</template>

<script setup>

import { ref } from 'vue';
import { useFlowersStore } from '../store/index';


let searchValue = ref("");
const store = useFlowersStore();
const flowers = store.flowers;


const searchFlowers = () => {
    return flowers.filter((flower) =>
        flower.description.toLowerCase().includes(searchValue.value.toLowerCase()));
}


</script>

<style lang="scss" scoped>
    .catalog {
        padding: 0 8rem;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 30px;

        &__search {
            width: 600px;
        }

        &__items {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
            margin-bottom: 30px;
        }

        &__item {
            width: 382px;
            height: 230px;
            object-fit: cover;
        }
    }
</style>