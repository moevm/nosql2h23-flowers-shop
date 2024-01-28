<template>
    <div className="flowerCard">
        <img 
            :src="flower.image"
            className="flowerCard__image"
        >

        <div className="flowerCard__info">
            <h2 class="flowerCard__title">
                {{ flower.name }}
            </h2>

            <p class="flowerCard__desc">
                {{ flower.description }}
            </p>

            <div className="flowerCard__options">
                <div className="flowerCard__optionsCount">
                    <img src="/icons/minus.svg"/>

                    1

                    <img src="/icons/plus.svg"/>
                </div>

                <span className="flowerCard__optionsPrice">
                    {{ flower.price }} ₽
                </span>
            </div>

            <button className="app_button" @click="store.addToCart(flower.id)">
                Добавить в корзину
            </button>
        </div>
        </div>
</template>

<script setup>
import { useFlowersStore } from '../store/index';

const store = useFlowersStore();
const flowers = store.flowers;
const flower = flowers.find(flower => flower.id == props.id);

const props = defineProps({
    id: {
        type: String,
        reqiered: true,
        default: 0
    }
})
</script>

<style lang="scss" scoped>
.flowerCard {
    border-radius: 15px;
    background: var(--color-white);
    margin: 50px 150px;
    padding: 50px;

    display: flex;
    align-items: center;
    justify-content: space-evenly;
    gap: 50px;

    &__image {
        width: 686px;
        height: 414px;
        object-fit: cover;
    }

    &__info {
        display: flex;
        flex-direction: column;
        gap: 50px;
    }

    &__title {
        color: var(--color-accent-pink);
        font-size: 27px;
        font-style: normal;
        text-transform: uppercase;
        font-weight: 400;
    }

    &__options {
        display: flex;
        justify-content: space-between;

        &Price {
            color: #000;
            font-size: 27px;
            font-style: normal;
            font-weight: 400;
        }
    }
}
</style>