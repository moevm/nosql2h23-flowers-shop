<template>
    <div className="cartItem">
        <!--! Добавить цикл для товаров из корзины -->
        <div 
            :v-for="item in products"
            className="cartItem__header"
        >
            <img :src="item.product.image" className="cartItem__image">

            <div className="cartItem__info">
                <h2 class="cartItem__title">
                    {{ item.product.name }}
                </h2>

                <div className="cartItem__options">
                    <span className="cartItem__amount">
                        Количество: {{ item.r.amount }}
                    </span>

                    <span className="cartItem__optionsPrice">
                        {{ item.r.cost }} ₽
                    </span>
                </div>
            </div>
        </div>

        <div className="divider"></div>

        <div className="cartItem__delivery">
            <span>Доставка</span>   

            <span>Бесплатно</span>
        </div>

        <div className="divider"></div>

        <div className="cartItem__cost">
            <span>Общая стоимость</span>

            <span> {{ order.cost }} </span>
            </div>
    </div>
</template>

<script setup>
import { useFlowersStore } from '../store/index';

const store = useFlowersStore();
const cart = store.cart; 
const order = cart[0];
const products = cart.splice(0, 1);
console.log(products);

</script>

<style lang="scss" scoped>
.cartItem {
    border-radius: 15px;
    background: var(--color-white);
    padding: 50px;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 20px;

    &__header {
        display: flex;
        gap: 20px;
    }

    &__image {
        width: 270px;
        height: 163px;
        object-fit: cover;
    }

    &__info {
        display: flex;
        flex-direction: column;
        gap: 30px;
    }

    &__title {
        font-size: 27px;
        font-style: normal;
        font-weight: 400;
    }

    &__options {
        display: flex;
        justify-content: space-between;
        font-size: 27px;

        &Price {
            color: #000;
            font-style: normal;
            font-weight: 400;
        }
    }

    &__delivery, 
    &__cost {
        font-size: 24px;
        display: flex;
        width: 100%;
        justify-content: space-between;
    }
}
</style>