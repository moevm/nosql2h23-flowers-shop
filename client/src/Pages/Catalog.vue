<template>
    <div className="catalog">
            <h2 className="section_title">
                Каталог
            </h2>

            <input 
                class="catalog__search"
                placeholder="Гортензии"
                v-model="searchValue"
            >

            <div className="catalog__items">
                <img 
                    class="catalog__item"
                    v-for="image in images" 
                    :key="image.id" 
                    :src="image.path"
                />
            </div>
        </div>
</template>

<script setup>
import { ref } from 'vue'

let searchValue = ref("");

const images = [
    {
        id: 1,
        path: "/images/slider1.jpg"
    },
    {
        id: 2,
        path: "/images/slider2.jpg"
    },
    {
        id: 3,
        path: "/images/slider3.jpg"
    },
    {
        id: 4,
        path: "/images/slider4.jpg"
    },
    {
        id: 5,
        path: "/images/slider1.jpg"
    },
    {
        id: 6,
        path: "/images/slider2.jpg"
    },
    {
        id: 7,
        path: "/images/slider3.jpg"
    },
    {
        id: 8,
        path: "/images/slider4.jpg"
    }
]
</script>

<style lang="scss" scoped>
    .catalog {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 30px;

        &__search {
            width: 600px;
            height: 50px;
            border-radius: 10px;
            border: 2px solid var(--color-dark-text);
            box-sizing: border-box;
            color: var(--color-dark-text);
            font-size: 22px;
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